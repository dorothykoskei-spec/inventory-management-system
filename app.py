from flask import Flask, jsonify, request

app = Flask(__name__)

mock_products = [
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
    },
    {
        "id": 2,
        "status": 1,
        "product": {
            "product_name": "Bread",
            "brands": "Broadways",
            "ingredients_text": "Flour, water, yeast, salt"
        },
        "price": 150,
        "stock": 15
    },
    {
        "id": 3,
        "status": 1,
        "product": {
            "product_name": "Sugar",
            "brands": "Kabras",
            "ingredients_text": "Sugar"
        },
        "price": 180,
        "stock": 20
    },
   
]

@app.route("/")
def home():
    return "Inventory Management API is running!"

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(mock_products)

@app.route("/inventory/<int:id>", methods=["GET"])
def get_product(id):
    for product in mock_products:
        if product["id"] == id:
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/inventory", methods=["POST"])
def add_product():
    data = request.get_json()
    new_product = {
        "id": len(mock_products) + 1,
        "status": 1,
        "product": {
            "product_name": data["product_name"],
            "brands": data["brands"],
            "ingredients_text": data["ingredients_text"]
        },
        "price": data.get("price", 0),
        "stock": data.get("stock", 0)
    }
    mock_products.append(new_product)
    return jsonify(new_product), 201


@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_product(id):
    data = request.get_json()

    for product in mock_products:
        if product["id"] == id:

            if "price" in data:
                product["price"] = data["price"]

            if "stock" in data:
                product["stock"] = data["stock"]

            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_product(id):
    for product in mock_products:
        if product["id"] == id:
            mock_products.remove(product)

            return jsonify({
                "message": "Product deleted successfully"
            })

    return jsonify({"error": "Product not found"}),404





if __name__ == "__main__":
    app.run(debug=True)
