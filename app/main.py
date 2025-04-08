"""Main FastAPI application module."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Root GET endpoint returning a message."""
    return {"message": "Hello, World!"}
