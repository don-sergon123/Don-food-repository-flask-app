import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_item(client):
    new_item = {"product_name": "Greek Yogurt",
                "brands": "Danone", "quantity": 5, "price": 120.0}
    response = client.post('/inventory', json=new_item)
    assert response.status_code == 201
    data = response.get_json()
    assert data["product_name"] == "Greek Yogurt"
