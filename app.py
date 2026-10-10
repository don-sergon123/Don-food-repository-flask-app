from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "product_name": "Long Life Milk",
        "brands": "Brookside",
        "quantity": 10,
        "price": 70.00
    },
    {
        "id": 2,
        "product_name": "Bread 800g",
        "brands": "Broadways",
        "quantity": 8,
        "price": 120.00
    }
]

# GET -> Fetch all items

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

# GET -> Fetch a single item
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# POST -> Add a new item
@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.get_json()
    if not data or 'product_name' not in data:
        return jsonify({"error": "Invalid input, product_name required"}), 400

    new_item = {
        "id": inventory[-1]["id"] + 1 if inventory else 1,
        "product_name": data.get("product_name"),
        "brands": data.get("brands", "Unknown"),
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0.0)
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

# PATCH -> Update an existing item
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item["product_name"] = data.get("product_name", item["product_name"])
    item["brands"] = data.get("brands", item["brands"])
    item["quantity"] = data.get("quantity", item["quantity"])
    item["price"] = data.get("price", item["price"])

    return jsonify(item), 200

# DELETE  -> Remove an item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory = [i for i in inventory if i["id"] != item_id]
    return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

def fetch_external_product(barcode_or_name):
    """Queries OpenFoodFacts API by barcode or product name."""
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode_or_name}.json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == 1:
                product_info = data.get("product", {})
                return {
                    "product_name": product_info.get("product_name"),
                    "brands": product_info.get("brands"),
                    "ingredients_text": product_info.get("ingredients_text")
                }
        return None
    except requests.exceptions.RequestException as e:
        print(f"API Connection Error: {e}")
        return None

