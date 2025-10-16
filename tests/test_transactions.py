# tests/test_transactions.py
import base64
import pytest
from datetime import datetime

@pytest.fixture
def auth_headers(test_user):
    credentials = base64.b64encode(b"testuser:testpassword").decode("utf-8")
    return {"Authorization": f"Basic {credentials}"}

def test_create_transaction(client, auth_headers):
    transaction_data = {
        "amount": 100.0,
        "description": "Test transaction",
        "category": "food",
        "type": "expense",
        "date": datetime.now().isoformat()
    }
    
    response = client.post("/transactions/", json=transaction_data, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 100.0
    assert data["description"] == "Test transaction"
    assert data["category"] == "food"
    assert data["type"] == "expense"
    assert "id" in data
    assert "user_id" in data

def test_get_transactions_empty(client, auth_headers):
    response = client.get("/transactions/", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == []

def test_get_transactions_with_data(client, auth_headers):
    # Сначала создаем транзакцию
    transaction_data = {
        "amount": 100.0,
        "description": "Test transaction",
        "category": "food",
        "type": "expense",
        "date": datetime.now().isoformat()
    }
    client.post("/transactions/", json=transaction_data, headers=auth_headers)
    
    # Затем получаем список
    response = client.get("/transactions/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["amount"] == 100.0

def test_delete_transaction(client, auth_headers, db_session):
    # Создаем транзакцию
    transaction_data = {
        "amount": 100.0,
        "description": "Test transaction",
        "category": "food",
        "type": "expense",
        "date": datetime.now().isoformat()
    }
    create_response = client.post("/transactions/", json=transaction_data, headers=auth_headers)
    transaction_id = create_response.json()["id"]
    
    # Удаляем транзакцию
    response = client.delete(f"/transactions/{transaction_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Transaction deleted successfully"}
    
    # Проверяем, что транзакция удалена
    get_response = client.get("/transactions/", headers=auth_headers)
    assert len(get_response.json()) == 0

def test_delete_nonexistent_transaction(client, auth_headers):
    response = client.delete("/transactions/999", headers=auth_headers)
    assert response.status_code == 404
    assert "Transaction not found" in response.json()["detail"]

def test_get_transactions_unauthorized(client):
    response = client.get("/transactions/")
    assert response.status_code == 401

def test_create_transaction_unauthorized(client):
    transaction_data = {
        "amount": 100.0,
        "description": "Test transaction",
        "category": "food",
        "type": "expense",
        "date": datetime.now().isoformat()
    }
    response = client.post("/transactions/", json=transaction_data)
    assert response.status_code == 401