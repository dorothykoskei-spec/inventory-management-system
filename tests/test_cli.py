from unittest.mock import patch, Mock

import cli


def test_show_menu(capsys):
    cli.show_menu()

    output = capsys.readouterr().out

    assert "INVENTORY MANAGEMENT SYSTEM" in output
    assert "1. Add new inventory item" in output
    assert "2. View inventory details" in output
    assert "3. Update item price or stock" in output
    assert "4. Delete product" in output
    assert "5. Find item on OpenFoodFacts" in output
    assert "6. Exit" in output


@patch("cli.requests.post")
def test_add_item(mock_post, monkeypatch):
    mock_post.return_value.status_code = 201

    answers = iter([
        "Milk",
        "200",
        "10"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    cli.add_item()

    mock_post.assert_called_once()


@patch("cli.requests.get")
def test_view_inventory(mock_get, capsys):
    mock_response = Mock()

    # Tell the fake response that the request was successful
    mock_response.status_code = 200

    mock_response.json.return_value = [
        {
            "id": 1,
            "product": {
                "product_name": "Milk"
            },
            "price": 200,
            "stock": 10
        }
    ]

    mock_get.return_value = mock_response

    cli.view_inventory()

    output = capsys.readouterr().out

    assert "Milk" in output
    assert "200" in output
    assert "10" in output


@patch("cli.requests.patch")
@patch("cli.view_inventory")
def test_update_item(mock_view, mock_patch, monkeypatch):
    answers = iter([
        "1",
        "1",
        "250"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers)
    )

    cli.update_item()

    mock_patch.assert_called_once()


@patch("cli.requests.delete")
@patch("cli.view_inventory")
def test_delete_item(mock_view, mock_delete, monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    cli.delete_item()

    mock_delete.assert_called_once()


@patch("cli.find_product_by_barcode")
def test_find_external_product(mock_find, monkeypatch, capsys):
    mock_find.return_value = {
        "product_name": "Nutella",
        "brands": "Ferrero",
        "code": "3017624010701",
        "quantity": "400g"
    }

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "3017624010701"
    )

    cli.find_external_product()

    output = capsys.readouterr().out

    assert "Nutella" in output
    assert "Ferrero" in output
    assert "3017624010701" in output