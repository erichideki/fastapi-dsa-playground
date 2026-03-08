from fastapi import FastAPI

from app.arrays.router import router as arrays_router

app = FastAPI(
    title="DSA FastAPI Playground",
    description="Practice data structures and algorithms using FastAPI",
    version="0.1.0"
)

app.include_router(arrays_router)


@app.get("/")
def root():
    return {"message": "DSA FastAPI Playground"}