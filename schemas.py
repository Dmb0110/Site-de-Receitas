from typing import Optional
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    password: str

########################################
class CriarReceita(BaseModel):
    nome_da_receita: str
    ingredientes: str
    modo_de_preparo: str

class ReceitaOut(BaseModel):
    id: int
    nome_da_receita: str
    ingredientes: str
    modo_de_preparo: str

    class Config:
        from_attributes = True

class Atualizar(BaseModel):
    nome_da_receita: Optional[str] = None
    ingredientes: Optional[str] = None
    modo_de_preparo: Optional[str] = None

class Deletar(BaseModel):
    mensagem: bool
