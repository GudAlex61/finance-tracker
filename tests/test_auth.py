# tests/test_auth.py
import base64

def test_register_user(client):
    user_data = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "newpassword"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "new@example.com"
    assert "id" in data
    assert "hashed_password" not in data

def test_register_duplicate_username(client, test_user):
    user_data = {
        "username": "testuser",  # уже существует
        "email": "new2@example.com",
        "password": "password"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert "Username already registered" in response.json()["detail"]

def test_register_duplicate_email(client, test_user):
    user_data = {
        "username": "newuser2",
        "email": "test@example.com",  # уже существует
        "password": "password"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]

def test_login_success(client, test_user):
    credentials = base64.b64encode(b"testuser:testpassword").decode("utf-8")
    headers = {"Authorization": f"Basic {credentials}"}
    
    response = client.post("/login", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"

def test_login_invalid_username(client):
    credentials = base64.b64encode(b"wronguser:password").decode("utf-8")
    headers = {"Authorization": f"Basic {credentials}"}
    
    response = client.post("/login", headers=headers)
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]

def test_login_invalid_password(client, test_user):
    credentials = base64.b64encode(b"testuser:wrongpassword").decode("utf-8")
    headers = {"Authorization": f"Basic {credentials}"}
    
    response = client.post("/login", headers=headers)
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]