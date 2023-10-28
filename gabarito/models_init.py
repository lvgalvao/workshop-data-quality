# models.py
from pydantic import BaseModel
from datetime import datetime
class Vendas(BaseModel):
    email: str
    data: datetime
    valor: int
    produto: str
    quantidade: int
    categoria: str