from http import HTTPStatus
from fastapi.testclient import TestClient
from app.main import app

def test_hello_world() -> None:
    client = TestClient(app)
    response = client.get(
        "/"
    )
    assert response.status_code == HTTPStatus.OK
    content = response.json()
    assert content['message'] == "Hello World"