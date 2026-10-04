# Inventory Management System

This is a simple **Inventory Management System** built with Python and Flask.

The project helps a user manage products in an inventory. The user can add products, view them, update their price or stock, and delete products.

The project also connects to the **Open Food Facts API** so that a user can search for product information using a barcode.

## What the Project Does

The system allows the user to:

* Add a new product to the inventory
* View all products
* View a specific product
* Update a product's price or stock
* Delete a product
* Search for product information using a barcode
* Use a CLI (Command Line Interface) to interact with the system

The inventory is currently stored in a Python list, which acts as our temporary/mock database.

## Technologies Used

* Python
* Flask
* Requests
* Pytest
* Open Food Facts API
* Git and GitHub

## Project Files

```text
inventory-management-system/
│
├── app.py
├── cli.py
├── openfoodfacts.py
├── requirements.txt
├── README.md
└── tests/
```

### What each file does

**app.py**

Contains the Flask application and the API routes for managing inventory.

**cli.py**

Contains the command-line interface. This is where the user can choose what they want to do with the inventory.

**openfoodfacts.py**

Connects my  application to the Open Food Facts API and gets product information using a barcode.

**tests/**

Contains the tests for the application.

## API Routes

Our Flask API has the following routes:

| Method | Route | What it does |
|--------|-------|--------------|
| GET | `/inventory` | Shows all inventory items |
| GET | `/inventory/<id>` | Shows one item |
| POST | `/inventory` | Adds a new item |
| PATCH | `/inventory/<id>` | Updates an item |
| DELETE | `/inventory/<id>` | Deletes an item |

## Open Food Facts API

I use the Open Food Facts API to find information about products.

The user enters a product barcode, and the application sends a request to the API.

For example:

```text
Enter product barcode: 3274080005003
```

The application displays information returned by the Open Food Facts API, such as:

```text
Product: isabelle
Brand: Cristaline
Barcode: 3274080005003
Quantity: 1500 ml
```

## CLI Menu

The project has a simple menu that allows the user to choose an action.

```text
================================
   INVENTORY MANAGEMENT SYSTEM
================================
1. Add new inventory item
2. View inventory details
3. Update item price or stock
4. Delete product
5. Find item on OpenFoodFacts
6. Exit
```

For example, if the user chooses 1, they can enter a product name, price, and stock quantity.

## Mock Inventory Data

For this project, we use a Python list as a temporary database.

Each product has an ID, name, price, stock, and other information.

Example:

```python
{
    "id": 1,
    "status": 1,
    "product": {
        "product_name": "Milk",
        "brands": "Brookside",
        "ingredients_text": "Milk"
    },
    "price": 250,
    "stock": 20
}
```

When a product is added, updated, or deleted, the list is changed.

## How to Run the Project

First, clone the project from GitHub and move into the project folder.

```bash
git clone https://github.com/dorothykoskei-spec/inventory-management-system.git
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Flask API

Start the Flask application:

```bash
python3 app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

The API routes can then be tested using a browser or Postman.

## Running the CLI

To start the command-line application, run:

```bash
python3 cli.py
```

The inventory menu will appear in the terminal.

## Running Tests

 I use **PYTHONPATH=. pytest** to test the project.

Run:

```bash
PYTHONPATH=. pytest
```

The tests check things such as:

* Adding inventory items
* Getting inventory items
* Updating items
* Deleting items
* CLI functionality
* Open Food Facts API requests


## Conclusion

This project helped me practice building a small application using Python and Flask. I learned how to create REST API routes, work with inventory data, use a CLI, connect to an external API, and write tests for my code.

