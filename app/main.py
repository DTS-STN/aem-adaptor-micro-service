from typing import Any, Dict, Union

import uvicorn
from fastapi import FastAPI
from app.routers import sch_router

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}


app.include_router(sch_router.router)


def start() -> None:
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
