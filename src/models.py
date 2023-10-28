from pydantic import BaseModel
from datetime import datetime

class Vendas(BaseModel):

    """
    Classe que representa o schema de vendas.

    args:
        email (str): Email do cliente.
        data (datetime): Data da compra.
        valor (float): Valor total da compra.
        produto (str): Nome do produto.
        quantidade (int): Quantidade do produto.
        categoria (str): Categoria do produto.
    
    examples:
        arquivo valido:
        
        ```json
        {
        "email": "cliente@example.com",
        "data": "2023-10-01T00:00:00",
        "valor": 150.0,
        "produto": "cadeira",
        "quantidade": 5,
        "categoria": "categoria1"
        }
        ```
    
    """
    email: str
    data: datetime
    valor: float
    produto: str
    quantidade: int
    categoria: str