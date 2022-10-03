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
    # read in env var for redis host, port, and db
    path = request.url.path.replace("/", "_")

    # establish redis connection
    r = redis.StrictRedis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        db=int(os.getenv("REDIS_DB", "0")),
        username=os.getenv("REDIS_USER"),
        password=os.getenv("REDIS_PASSWORD"),
    )

    # check redis for values
    if r.exists(path) and path != "":
        # if a key is found, return the value
        return JSONResponse(json.loads(r.get(path)))

    response = await call_next(request)

    # if no key is found, and the response is good then the request proceeds
    if response.status_code == 200:
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        json_decoded = json.loads((b"".join(response_body)).decode())

        r.set(path, json.dumps(json_decoded))

        return JSONResponse(json_decoded)

    # if the value is not cached, and the value is not status 200, then just return the response
    return response


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


app.include_router(sch_router.router)


def start() -> None:
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
