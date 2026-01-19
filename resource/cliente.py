from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models.cliente import ClienteModel
from schemas.cliente import ClienteSchema, ClienteSchemaUpdate

cliente_blp = Blueprint(
    "Cliente",
    __name__,
    description="Operações relacionadas a clientes"
)


@cliente_blp.route("/clientes")
class ClienteLista(MethodView):
    @cliente_blp.response(200, ClienteSchema(many=True))
    def get(self):
        """Lista todos os clientes"""
        return ClienteModel.query.all()

    @cliente_blp.arguments(ClienteSchema)
    @cliente_blp.response(201, ClienteSchema)
    def post(self, cliente_dados):
        """Cria um novo cliente"""
        # Verifica se email já existe
        if ClienteModel.query.filter_by(email=cliente_dados['email']).first():
            abort(409, message="Email já cadastrado")

        cliente = ClienteModel(**cliente_dados)
        
        db.session.add(cliente)
        db.session.commit()
        return cliente


@cliente_blp.route("/clientes/<int:cliente_id>")
class ClienteId(MethodView):
    @cliente_blp.response(200, ClienteSchema)
    def get(self, cliente_id):
        """Busca cliente por ID"""
        cliente = ClienteModel.query.get(cliente_id)
        if not cliente:
            abort(404, message="Cliente não encontrado")
        return cliente

    @cliente_blp.arguments(ClienteSchemaUpdate)
    @cliente_blp.response(200, ClienteSchema)
    def put(self, dados_atualizados, cliente_id):
        """Atualiza cliente por ID"""
        cliente = ClienteModel.query.get(cliente_id)
        if not cliente:
            abort(404, message="Cliente não encontrado")

        # Atualiza os campos
        for key, value in dados_atualizados.items():
            setattr(cliente, key, value)

        db.session.commit()
        return cliente

    @cliente_blp.arguments(ClienteSchemaUpdate)
    @cliente_blp.response(200, ClienteSchema)
    def patch(self, dados_atualizados, cliente_id):
        """Atualiza cliente parcialmente por ID"""
        cliente = ClienteModel.query.get(cliente_id)
        if not cliente:
            abort(404, message="Cliente não encontrado")

        # Atualiza apenas os campos enviados
        for key, value in dados_atualizados.items():
            setattr(cliente, key, value)

        db.session.commit()
        return cliente

    @cliente_blp.response(200)
    def delete(self, cliente_id):
        """Remove cliente por ID"""
        cliente = ClienteModel.query.get(cliente_id)
        if not cliente:
            abort(404, message="Cliente não encontrado")

        db.session.delete(cliente)
        db.session.commit()
        return {"message": "Cliente removido com sucesso"}