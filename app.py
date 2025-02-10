from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados (podem representar um banco de dados ou qualquer fonte de dados)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800},
    {"id": 3, "name": "Headphones", "price": 200}
]

# Rotas
@app.route('/users', methods=['GET'])
def get_users():
    """Retorna a lista de usuários."""
    return jsonify(users), 200

@app.route('/products', methods=['GET'])
def get_products():
    """Retorna a lista de produtos."""
    return jsonify(products), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retorna os detalhes de um único usuário pelo ID."""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retorna os detalhes de um único produto pelo ID."""
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route('/user', methods=['POST'])
def create_user():
    """Cria um novo usuário."""
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Invalid input"}), 400
   
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/product', methods=['POST'])
def create_product():
    """Cria um novo produto."""
    data = request.get_json()
    if not data.get("name") or not data.get("price"):
        return jsonify({"error": "Invalid input"}), 400
   
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Rota raiz para verificar o funcionamento
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API está funcionando!"}), 200

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
