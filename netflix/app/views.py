from flask import Blueprint, jsonify, request
from .models import Cliente, db

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/cliente", methods=["GET"])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes]), 200

@cliente_bp.route("/cliente", methods=["POST"])
def insert_cliente():
    dados = request.get_json()
    name = dados.get("name")
    email = dados.get("email")
    plano = dados.get("plano")
    
    if not name or not email:
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400
    
    novo_cliente = Cliente(name,email,plano)
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify(novo_cliente.to_dict()), 201