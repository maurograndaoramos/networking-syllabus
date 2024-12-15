from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    if 0 <= item_id < len(items):
        items[item_id] = updated_item
        return jsonify(updated_item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        deleted_item = items.pop(item_id)
        return jsonify(deleted_item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)