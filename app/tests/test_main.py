from http import HTTPStatus
from fastapi.testclient import TestClient
from app.main import app


def test_vowel_count() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.post("/vowel_count", json=data)
    content = response.json()
    assert content == {"batman": 2, "robin": 2, "coringa": 3}


def test_vowel_count_bad_request() -> None:
    client = TestClient(app)
    data = {"words": 123}
    response = client.post("/vowel_count", json=data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    content = response.json()
    assert content["detail"][0]["msg"] == "Input should be a valid list"


def test_vowel_count_with_invalid_content_type() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.post(
        "/vowel_count", headers={"Content-Type": "application/text"}, json=data
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_vowel_count_with_invalid_route_name() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"]}
    response = client.post(
        "/vowel_count_not_found",
        headers={"Content-Type": "application/json"},
        json=data,
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_vowel_count_with_invalid_http_method() -> None:
    client = TestClient(app)
    response = client.get("/vowel_count", headers={"Content-Type": "application/json"})
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_vowel_count_with_invalid_request_body() -> None:
    client = TestClient(app)
    data = {"words": [1, 2, 3]}
    response = client.post(
        "/vowel_count", headers={"Content-Type": "application/json"}, json=data
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_sort_asc() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"], "order": "asc"}
    response = client.post("/sort", json=data)
    content = response.json()
    assert content == ["batman", "coringa", "robin"]


def test_sort_desc() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"], "order": "desc"}
    response = client.post("/sort", json=data)
    content = response.json()
    assert content == ["robin", "coringa", "batman"]


def test_sort_with_invalid_order() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"], "order": "invalid"}
    response = client.post("/sort", json=data)
    content = response.json()
    assert content["detail"][0]["msg"] == "Input should be 'asc' or 'desc'"


def test_sort_bad_requst() -> None:
    client = TestClient(app)
    data = {"words": 123, "order": "invalid"}
    response = client.post("/sort", json=data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    content = response.json()
    assert content["detail"][0]["msg"] == "Input should be a valid list"


def test_sort_with_invalid_content() -> None:
    client = TestClient(app)
    data = {"words": ["batman", "robin", "coringa"], "order": "invalid"}
    response = client.post(
        "/sort", headers={"Content-Type": "application/pdf"}, json=data
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_sort_with_invalid_http_method() -> None:
    client = TestClient(app)
    response = client.get(
        "/sort",
    )
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_sort_with_invalid_request_body() -> None:
    client = TestClient(app)
    data = {"words": [1, 2, 3], "order": "invalid"}
    response = client.post("/sort", json=data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
