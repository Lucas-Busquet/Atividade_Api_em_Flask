from db import db
from datetime import datetime


class ClienteModel(db.Model):
    __tablename__ = "clientes"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamento 1-N: Cliente → Pedidos
    pedidos = db.relationship(
        "PedidoModel",
        back_populates="cliente",
        lazy="dynamic",
        cascade="all, delete-orphan"
    )