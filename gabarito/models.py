# models.py
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum
from typing import Optional

class CategoriaEnum(str, Enum):
    categoria1 = "categoria1"
    categoria2 = "categoria2"
    categoria3 = "categoria3"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto: Optional[str] = None
    quantidade: PositiveInt
    categoria: CategoriaEnum

    @validator('categoria')
    def categoria_deve_estar_no_enum(cls, error):
        return error