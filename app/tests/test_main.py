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

def test_vowel_count() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.post(
        "/vowel_count",
        json=data
    )
    content = response.json()
    assert content == {"batman": 2, "robin": 2, "coringa": 3}

    
