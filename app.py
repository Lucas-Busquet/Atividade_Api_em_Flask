from flask import Flask
from flask_smorest import Api
from db import db
from resource.cliente import cliente_blp
from resource.pedido import pedido_blp

app = Flask(__name__)

# Configurações da API e Swagger
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "API de Gestão de Clientes e Pedidos"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Configuração do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar extensões
db.init_app(app)
api = Api(app)

# Registrar Blueprints
api.register_blueprint(cliente_blp)
api.register_blueprint(pedido_blp)

# Criar tabelas antes da primeira requisição
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)