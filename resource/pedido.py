from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models.pedido import PedidoModel
from models.cliente import ClienteModel
from schemas.pedido import PedidoSchema, PedidoSchemaUpdate

pedido_blp = Blueprint(
    "Pedido",
    __name__,
    description="Operações relacionadas a pedidos"
)


@pedido_blp.route("/pedidos")
class PedidoLista(MethodView):
    @pedido_blp.response(200, PedidoSchema(many=True))
    def get(self):
        """Lista todos os pedidos"""
        return PedidoModel.query.all()

    @pedido_blp.arguments(PedidoSchema)
    @pedido_blp.response(201, PedidoSchema)
    def post(self, pedido_dados):
        """Cria um novo pedido"""
        # Valida se o cliente existe
        cliente = ClienteModel.query.get(pedido_dados['cliente_id'])
        if not cliente:
            abort(404, message="Cliente não encontrado")

        pedido = PedidoModel(**pedido_dados)
        
        db.session.add(pedido)
        db.session.commit()
        return pedido


@pedido_blp.route("/pedidos/<int:pedido_id>")
class PedidoId(MethodView):
    @pedido_blp.response(200, PedidoSchema)
    def get(self, pedido_id):
        """Busca pedido por ID"""
        pedido = PedidoModel.query.get(pedido_id)
        if not pedido:
            abort(404, message="Pedido não encontrado")
        return pedido

    @pedido_blp.arguments(PedidoSchemaUpdate)
    @pedido_blp.response(200, PedidoSchema)
    def put(self, dados_atualizados, pedido_id):
        """Atualiza pedido por ID"""
        pedido = PedidoModel.query.get(pedido_id)
        if not pedido:
            abort(404, message="Pedido não encontrado")

        # Atualiza os campos
        for key, value in dados_atualizados.items():
            setattr(pedido, key, value)

        db.session.commit()
        return pedido

    @pedido_blp.arguments(PedidoSchemaUpdate)
    @pedido_blp.response(200, PedidoSchema)
    def patch(self, dados_atualizados, pedido_id):
        """Atualiza pedido parcialmente por ID"""
        pedido = PedidoModel.query.get(pedido_id)
        if not pedido:
            abort(404, message="Pedido não encontrado")

        # Atualiza apenas os campos enviados
        for key, value in dados_atualizados.items():
            setattr(pedido, key, value)

        db.session.commit()
        return pedido

    @pedido_blp.response(200)
    def delete(self, pedido_id):
        """Remove pedido por ID"""
        pedido = PedidoModel.query.get(pedido_id)
        if not pedido:
            abort(404, message="Pedido não encontrado")

        db.session.delete(pedido)
        db.session.commit()
        return {"message": "Pedido removido com sucesso"}