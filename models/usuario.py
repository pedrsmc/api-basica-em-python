from pydantic import BaseModel, Field

class Usuario (BaseModel):
    id: str
    nome: str
    email: str
    tel: str
    idade: int
    
class UsuarioCreate (BaseModel):
    nome: str
    email: str
    tel: str
    idade: int

class UsuarioUpdate (BaseModel):
    nome: str | None = None
    email: str | None = None
    tel: str | None = None
    idade: int | None = None

