from fastapi.testclient import TestClient
from app.main import app

def test_health():
    client = TestClient(app)
    
    #response = client.get("/health") → sends a 
    # GET request to the /health endpoint.
    
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    from fastapi.testclient import TestClient
from app.main import app


def test_health():
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
