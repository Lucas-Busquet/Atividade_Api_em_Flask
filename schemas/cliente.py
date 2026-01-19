from marshmallow import Schema, fields

class ClienteSchema(Schema):
    """Schema completo para criar/retornar cliente"""
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    email = fields.Str(required=True)
    telefone = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)


class ClienteSchemaUpdate(Schema):
    """Schema para atualização parcial (PATCH/PUT)"""
    nome = fields.Str(required=False)
    email = fields.Str(required=False)
    telefone = fields.Str(required=False)