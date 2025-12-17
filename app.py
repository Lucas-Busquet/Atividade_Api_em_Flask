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

# GET /Clientes/1
@app.get('/clientes/<int:cliente_id>')
def obter_cliente_por_id(cliente_id):
    
    for cliente in clientes:
        if cliente["cliente_id"] == cliente_id:
            return jsonify(cliente), 200

    return jsonify({"erro": "Cliente não encontrado"}), 404