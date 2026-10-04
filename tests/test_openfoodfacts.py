from unittest.mock import patch

from openfoodfacts import find_product_by_barcode


def test_find_product():
    fake_data = {
        "status": "success",
        "product": {
            "product_name": "Milk",
            "brands": "Brookside"
        }
    }

    with patch("openfoodfacts.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = fake_data

        product = find_product_by_barcode("123456789")

        assert product["product_name"] == "Milk"
        assert product["brands"] == "Brookside"


def test_product_not_found():
    fake_data = {
        "status": "failure"
    }

    with patch("openfoodfacts.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = fake_data

        product = find_product_by_barcode("999999999")

        assert product is None