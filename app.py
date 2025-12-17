from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = [
    {
        'cliente_id': 1,
        'nome': 'Matheus Nogueira',
        'email': 'matheus_nogueira@email.com',
        'telefone': '11987654321'
    },
    {
        'cliente_id': 2,
        'nome': 'Lucas Busquet',
        'email': 'lucas_busquet@email.com',
        'telefone': '21912345678'
    }
]
next_id = 3 # Controlador de ID para o POST

if __name__ == '__main__':
    app.run(debug=True)

#GET / Clientes
@app.get('/clientes')
def get_clientes():
    return jsonify(clientes), 200  

# Buscar Cliente por ID
@app.get('/clientes/<int:cliente_id>')
def obter_cliente_por_id(cliente_id):
    
    for cliente in clientes:
        if cliente['cliente_id'] == cliente_id:
            return jsonify(cliente), 200
    return jsonify({'mensagem': 'Cliente não encontrado'}), 404  

# Criar Nova Cliente
@app.post('/clientes')
def criar_novo_cliente():
    global next_id
    novo_cliente = request.get_json()

    if not novo_cliente.get('nome') or not novo_cliente.get('email') or not novo_cliente.get('telefone'):
        return jsonify({'mensagem': 'Nome, email e telefone são obrigatórios'}), 400
    
    novo_cliente={
        'cliente_id': next_id,
        'nome': novo_cliente['nome'],
        'email': novo_cliente['email'],
        'telefone': novo_cliente['telefone']
    }

    clientes.append(novo_cliente)
    next_id += 1
    return jsonify(novo_cliente), 201

# Atualizar Cliente por ID
@app.put('/clientes/<int:cliente_id>')
def atualizar_cliente_por_id(cliente_id):
    dados_atualizados = request.get_json()
    
    if not dados_atualizados or (not dados_atualizados.get('nome') and not dados_atualizados.get('email') and not dados_atualizados.get('telefone')):
        return jsonify({'mensagem': 'Pelo menos um dos campos nome, email ou telefone deve ser fornecido para atualização'}), 400
    
    for cliente in clientes:
        if cliente['cliente_id'] == cliente_id:
            cliente['nome'] = dados_atualizados.get('nome', cliente['nome'])
            cliente['email'] = dados_atualizados.get('email', cliente['email'])
            cliente['telefone'] = dados_atualizados.get('telefone', cliente['telefone'])
            return jsonify(cliente), 200
    return jsonify({'mensagem': 'Cliente não encontrado'}), 404

# Deletar Cliente por ID
@app.delete('/clientes/<int:cliente_id>')
def deletar_cliente_por_id(cliente_id):
    global clientes
    cliente_remove = None

    for cliente in clientes:
        if cliente['cliente_id'] == cliente_id:
            cliente_remove = cliente
            break

    if cliente_remove is None:
        return jsonify({'mensagem': 'Cliente não encontrado'}), 404
    
    clientes.remove(cliente_remove)

    return jsonify({'mensagem': 'Cliente deletado com sucesso'}), 200
