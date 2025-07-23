from flask import Flask, request, jsonify
import sqlite3
from mistral_model import ask_agent
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend access

DB_PATH = 'ecommerce.db'

# --- ROUTES ---

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    # Call Mistral model (via helper)
    ai_response = ask_agent(user_message)

    return jsonify({"reply": ai_response})


@app.route("/api/products", methods=["GET"])
def get_products():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, price FROM products")
    rows = cursor.fetchall()
    conn.close()

    products = [{"id": r[0], "name": r[1], "price": r[2]} for r in rows]
    return jsonify(products)


@app.route("/api/product/<int:product_id>", methods=["GET"])
def get_product_detail(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        keys = ["id", "name", "description", "price", "stock"]
        product = dict(zip(keys, row))
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
