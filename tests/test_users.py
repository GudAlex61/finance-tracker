# tests/test_users.py
import base64

def test_get_current_user(client, test_user):
    credentials = base64.b64encode(b"testuser:testpassword").decode("utf-8")
    headers = {"Authorization": f"Basic {credentials}"}
    
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"

def test_get_current_user_unauthorized(client):
    response = client.get("/users/me")
    assert response.status_code == 401
    assert "Not authenticated" in response.json()["detail"]