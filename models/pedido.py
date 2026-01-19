from db import db
from datetime import datetime


class PedidoModel(db.Model):
    __tablename__ = "pedidos"
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="pendente")  # pendente, confirmado, cancelado
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign Key para Cliente
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id", ondelete="CASCADE"), nullable=False)
    
    # Relacionamento N-1: Pedido → Cliente
    cliente = db.relationship("ClienteModel", back_populates="pedidos")