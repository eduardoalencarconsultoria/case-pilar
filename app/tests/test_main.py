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

def test_vowel_count_bad_request() -> None:
    client = TestClient(app)
    data = {"words": 123}
    response = client.post(
        "/vowel_count",
        json=data
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY 
    content = response.json()
    assert content['detail'][0]['msg'] == "Input should be a valid list"

def test_vowel_count_with_invalid_content_type() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.post(
        "/vowel_count",
        headers={'Content-Type': 'application/text'},
        json=data
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY 
    
def test_vowel_count_with_invalid_route_name() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.post(
        "/vowel_count_not_found",
        headers={'Content-Type': 'application/json'},
        json=data
    )
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_vowel_count_with_invalid_http_method() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.get(
        "/vowel_count",
        headers={'Content-Type': 'application/json'}
    )
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED