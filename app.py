from flask import Flask, jsonify, request
from flask_smorest import abort
import uuid

from db import clientes

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# GET /clientes - Lista todos os clientes
@app.get('/clientes')
def get_clientes():
    return jsonify({"Clientes": list(clientes.values())}), 200  

# GET /cliente/<id> - Buscar Cliente por ID
@app.get('/cliente/<string:cliente_id>')
def obter_cliente_por_id(cliente_id):
    try:
        return jsonify(clientes[cliente_id]), 200
    except KeyError:
        abort(404, message="Cliente não encontrado")

# GET /cliente?nome=João - Buscar Cliente por nome (query parameter)
@app.get('/cliente')
def get_cliente_por_nome():
    nome = request.args.get('nome')
    
    if not nome:
        abort(400, message="Parâmetro 'nome' é obrigatório")
    
    for cliente in clientes.values():
        if cliente['nome'] == nome:
            return jsonify(cliente), 200
    
    abort(404, message="Cliente não encontrado")

# POST /cliente - Criar Novo Cliente
@app.post('/cliente')
def criar_novo_cliente():
    cliente_dado = request.get_json()

    if not cliente_dado.get('nome') or not cliente_dado.get('email') or not cliente_dado.get('telefone'):
        abort(400, message="Nome, email e telefone são obrigatórios")
    
    cliente_id = uuid.uuid4().hex
    
    cliente_novo = {**cliente_dado, "id": cliente_id}

    clientes[cliente_id] = cliente_novo
    
    return jsonify(cliente_novo), 201

# PUT /cliente/<id> - Atualizar Cliente por ID
@app.put('/cliente/<string:cliente_id>')
def atualizar_cliente_por_id(cliente_id):
    dados_atualizados = request.get_json()
    
    if not dados_atualizados or (not dados_atualizados.get('nome') and not dados_atualizados.get('email') and not dados_atualizados.get('telefone')):
        abort(400, message="Pelo menos um dos campos nome, email ou telefone deve ser fornecido para atualização")
    
    for cliente in clientes.values():
        if cliente['id'] == cliente_id:
            cliente.update(dados_atualizados)
            return jsonify({"cliente atualizado": cliente}), 200
    
    abort(404, message="Cliente não encontrado")

# DELETE /cliente/<id> - Deletar Cliente por id
@app.delete('/cliente/<string:cliente_id>')
def deletar_cliente_por_id(cliente_id):
    try:
        clientes.pop(cliente_id)
        return jsonify({"message": "Cliente removido com sucesso"}), 200
    except KeyError:
        abort(404, message="Cliente não encontrado")