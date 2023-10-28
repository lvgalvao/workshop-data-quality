# models.py
from pydantic import BaseModel
from datetime import datetime
class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (str): email do comprador
        data (datetime): data da compra
        valor (int): valor da compra
        produto (str): nome do produto
        quantidade (int): quantidade de produtos
        categoria (str): categoria do produto

    Example:
        Arquivo valido: 

        ```json
        {
            "email": "cliente@example.com",
            "data": "2023-10-01T00:00:00",
            "valor": 150.0,
            "produto": Cadeira,
            "quantidade": 5,
            "categoria": "categoria1"
        }
        ```
    """
    email: str
    data: datetime
    valor: int
    produto: str
    quantidade: int
    categoria: str