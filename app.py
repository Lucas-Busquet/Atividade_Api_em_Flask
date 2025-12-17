from flask import Flask, jsonify, request

app = Flask(__name__)

# BASE DE DADOS EM MEMÓRIA (Clientes)
clientes = [
    {
        'cliente_id': 1,
        'nome': 'João Silva',
        'email': 'joao.silva@email.com',
        'telefone': '11987654321'
    },
    {
        'cliente_id': 2,
        'nome': 'Maria Souza',
        'email': 'maria.souza@email.com',
        'telefone': '21912345678'
    }
]
next_id = 3 # Contador de ID para novos clientes

# --- ROTAS DA API ---

# Aqui entrarão as rotas (Passos 3 a 7)

# --- FIM DAS ROTAS ---

if __name__ == "__main__":
    app.run(debug=True) 
    