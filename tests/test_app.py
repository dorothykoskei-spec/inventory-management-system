import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200


def test_get_one_item(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200


def test_add_item(client):
    item = {
        "product_name": "Milk",
        "brands": "Brookside",
        "ingredients_text": "Milk",
        "price": 250,
        "stock": 10
    }

    response = client.post("/inventory", json=item)

    assert response.status_code == 201


def test_update_item(client):
    item = {
        "price": 300
    }

    response = client.patch("/inventory/1", json=item)

    assert response.status_code == 200


def test_delete_item(client):
    response = client.delete("/inventory/1")

    assert response.status_code == 200