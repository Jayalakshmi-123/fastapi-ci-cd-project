"""Main FastAPI application module."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Root GET endpoint returning a message."""
    return {"message": "Hello, World! i am bhaskar"}
@app.get("/feature")
def feature_endpoint():
    """Feature endpoint for demo purposes."""
    return {"message": "This is from a feature branch!"}
