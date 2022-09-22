import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
