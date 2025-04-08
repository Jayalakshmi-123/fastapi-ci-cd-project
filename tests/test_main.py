from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_feature_endpoint():
    response = client.get("/feature")
    assert response.status_code == 200
    assert response.json() == {"message": "This is from a feature branch!"}

