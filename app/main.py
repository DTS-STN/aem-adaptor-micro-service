import uvicorn
from fastapi import FastAPI
from app.routers import sch_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(sch_router.router)

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
