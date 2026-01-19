from marshmallow import Schema, fields

class PedidoSchema(Schema):
    """Schema completo para criar/retornar pedido"""
    id = fields.Int(dump_only=True)
    descricao = fields.Str(required=True)
    valor = fields.Float(required=True)
    status = fields.Str(required=False)
    created_at = fields.DateTime(dump_only=True)
    cliente_id = fields.Int(required=True, load_only=True)


class PedidoSchemaUpdate(Schema):
    """Schema para atualização parcial (PATCH/PUT)"""
    descricao = fields.Str(required=False)
    valor = fields.Float(required=False)
    status = fields.Str(required=False)
