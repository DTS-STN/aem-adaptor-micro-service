"""Adaptor for AEM Sanity"""

import json
import logging
import os
from typing import Any, Union

import redis
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel, BaseSettings
from starlette.concurrency import iterate_in_threadpool
from starlette.responses import JSONResponse, StreamingResponse

from app.lib.utils.utils import strtobool
from app.routers import sch_router


class Settings(BaseSettings):
    """FastAPI shared settings/functions"""

    cache: Any
    prod: bool = True
    cache_connected: bool = False


class BasicMessage(BaseModel):
    """Simple response string"""

    message: str


settings = Settings()

settings.prod = bool(strtobool(os.getenv("ISPROD", "True")))

if not settings.prod:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

# Create a redis connection pool, by reading in env vars
pool = redis.ConnectionPool(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    db=int(os.getenv("REDIS_DB", "0")),
    username=os.getenv("REDIS_USER"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

# establish redis connection
cache = redis.Redis(connection_pool=pool)

settings.cache_connected = cache.ping()

app = FastAPI()


@app.middleware("http")
async def handle_cache(request: Request, call_next: Any) -> Union[Any, None]:
    """Middleware that automates cache handling in request/response"""

    # establish naming convention for cache keys
    # this will likely need to be revised to include request.url.query
    cache_key = "home" + request.url.path.rstrip("/").replace("/", "_")

    # check redis for values
    if settings.cache_connected and cache.exists(cache_key):
        # if a key is found, return the value
        val = cache.get(cache_key)
        if not settings.prod:
            logger.debug("Using cache value for: %s", cache_key)

        if val is not None:
            return JSONResponse(
                content=json.loads(val),
                status_code=200,
            )

    # if no key is found, continue on with the request and await the response
    response = await call_next(request)

    # if the response is successful, then place the json value into the cache
    if settings.cache_connected and response.status_code == 200:
        if isinstance(response, StreamingResponse):
            response_body = [chunk async for chunk in response.body_iterator]
            response.body_iterator = iterate_in_threadpool(iter(response_body))

            # the response SHOULD be in bytes, but if it's not it'd be in a string
            # you can't assert an instance of a list, we could write our own class,
            # or we could do what I've done here, and ensured that the types match
            # their join methods. Mypy doesn't like that, but it is typesafe
            if all(isinstance(elements, bytes) for elements in response_body):
                json_val = json.loads((b"".join(response_body)).decode())  # type: ignore
            elif all(isinstance(elements, str) for elements in response_body):
                json_val = json.loads(("".join(response_body)).decode())  # type: ignore

        if isinstance(response, JSONResponse):
            json_val = response.body

        # place value in the cache, after combining it
        cache.set(cache_key, json.dumps(json_val))

    # if the value is not cached, and the value is not status 200, then just return the response
    return response


@app.get("/")
async def root() -> BasicMessage:
    """root is a placeholder that just says hello world"""

    return BasicMessage(message="Hello World")


app.include_router(sch_router.router)


def start() -> None:
    """starts the server, utilized primarily via poetry"""

    uvicorn.run(
        "app.main:app",
        host=os.getenv("APP_HOST", "127.0.0.1"),
        port=int(os.getenv("APP_PORT", "8000")),
        reload=bool(strtobool(os.getenv("APP_RELOAD", "True"))),
    )
