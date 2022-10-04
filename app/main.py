import json
import os
from typing import Any, Dict, Union

import redis
import uvicorn
from fastapi import FastAPI, Request
from starlette.concurrency import iterate_in_threadpool
from starlette.responses import JSONResponse, StreamingResponse

from app.routers import sch_router

app = FastAPI()


@app.middleware("http")
async def handle_cache(request: Request, call_next: Any) -> Union[Any, None]:
    # establish naming convention for cache keys, this will likely need to be revised to include request.url.query
    cache_key = "home" + request.url.path.rstrip("/").replace("/", "_")

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
    r = redis.Redis(connection_pool=pool)

    # check redis for values
    if r.exists(cache_key):
        # if a key is found, return the value
        val = r.get(cache_key)
        if val is not None:
            return JSONResponse(
                content=json.loads(val),
                status_code=200,
            )

    # if no key is found, continue on with the request and await the response
    response = await call_next(request)

    # if the response is successful, then place the json value into the cache
    if response.status_code == 200:
        if type(response) is StreamingResponse:
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

        if type(response) is JSONResponse:
            json_val = response.body

        # place value in the cache, after combining it
        r.set(cache_key, json.dumps(json_val))

    # if the value is not cached, and the value is not status 200, then just return the response
    return response


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


app.include_router(sch_router.router)


def start() -> None:
    uvicorn.run(
        "app.main:app",
        host=os.getenv("LOCAL_HOST", "127.0.0.1"),
        port=int(os.getenv("LOCAL_PORT", 8000)),
        reload=bool(os.getenv("LOCAL_RELOAD", True)),
    )
