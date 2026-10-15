import requests
import pytest
from test_data import valid_post, updated_post, partial_update


def test_get_post(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != ""
    assert data["body"] != ""


def test_get_nonexistent_post(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/9999",
        timeout=10
    )

    assert response.status_code == 404


def test_get_all_posts(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 100


def test_post_response_structure(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


@pytest.mark.parametrize("post_id", [1, 2, 3, 10, 50])
def test_get_post_by_id(api_base_url, post_id):
    response = requests.get(
        f"{api_base_url}/posts/{post_id}",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


@pytest.mark.parametrize("post_id", [0, -1, 9999])
def test_get_invalid_post_ids(api_base_url, post_id):
    response = requests.get(
        f"{api_base_url}/posts/{post_id}",
        timeout=10
    )

    assert response.status_code == 404



def test_create_post(api_base_url):
    response = requests.post(
        f"{api_base_url}/posts",
        json=valid_post,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == valid_post["title"]
    assert data["body"] == valid_post["body"]
    assert data["userId"] == valid_post["userId"]
    assert "id" in data


def test_update_post_put(api_base_url):
    payload = {
        "id": 1,
        "title": "Updated SDET Title",
        "body": "Updated post content",
        "userId": 1
    }

    response = requests.put(
        f"{api_base_url}/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_update_post_patch(api_base_url):
    payload = {
        "title": "Partially Updated Title"
    }

    response = requests.patch(
        f"{api_base_url}/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]



def test_delete_post(api_base_url):
    response = requests.delete(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200



def test_response_content_type(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]


def test_response_time(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3


def test_response_headers(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200
    assert "Content-Type" in response.headers
    assert "Cache-Control" in response.headers
