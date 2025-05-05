import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="session")
def user_data():
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    email = f"{username}@example.com"
    password = "testpass"
    response = client.post("/users/register", json={
        "username": username,
        "email": email,
        "password": password
    })
    assert response.status_code in (200, 201, 400), response.text
    return {"username": username, "email": email, "password": password}

def get_token(user_data):
    # ВАЖНО: используем email для логина!
    response = client.post("/users/login", data={
        "username": user_data["email"],
        "password": user_data["password"]
    })
    assert response.status_code == 200, response.text
    return response.json()["access_token"]

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Book Catalog API"}

def test_login_user(user_data):
    token = get_token(user_data)
    assert token is not None

def test_create_author(user_data):
    token = get_token(user_data)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/authors/", json={
        "name": "Test Author",
        "biography": "Test biography"
    }, headers=headers)
    assert response.status_code in (200, 201), response.text
    data = response.json()
    assert "id" in data

def test_create_book(user_data):
    token = get_token(user_data)
    headers = {"Authorization": f"Bearer {token}"}
    author_response = client.post("/authors/", json={
        "name": "Author For Book",
        "biography": "Bio"
    }, headers=headers)
    assert author_response.status_code in (200, 201), author_response.text
    author_id = author_response.json()["id"]

    response = client.post("/books/", json={
        "title": "Test Book",
        "description": "Test Description",
        "rating": 4.5,
        "author_id": author_id
    }, headers=headers)
    assert response.status_code in (200, 201), response.text
    data = response.json()
    assert "id" in data

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_authors():
    response = client.get("/authors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
