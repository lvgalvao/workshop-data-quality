from pydantic import BaseModel, ConfigDict, EmailStr, validator, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum
from typing import Optional

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"
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
    
    model_config = ConfigDict(extra='forbid')
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: Optional[str] = None
    quantidade: PositiveInt
    categoria: CategoriaEnum

    @validator('categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error