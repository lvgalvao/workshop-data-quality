from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validator
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"


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
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    categoria: CategoriaEnum

    @validator('categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error
    