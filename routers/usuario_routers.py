from fastapi import APIRouter, HTTPException
from models.usuario import UsuarioCreate, UsuarioUpdate
from services.usuario_service import (
    listarUsuarios,
    buscarUsuario,
    cadastrarUsuario,
    deletarUsuario,
    atualizarUsuario
)

msg = "ID de usuário não encontrado."
router = APIRouter()

@router.get("/")
def pag_inicial():
    return {"msg": "A API está rodando..."}

@router.get("/usuarios")
def get_usuarios():
    return listarUsuarios()

@router.get("/usuarios/{id}")
def get_usuario(id: str):
    usuarioEncontrado = buscarUsuario(id)
    
    if not usuarioEncontrado:
        raise HTTPException(status_code=404, detail=msg)
    return usuarioEncontrado

@router.post("/usuarios")
def post_usuario(usuario: UsuarioCreate):
    return cadastrarUsuario(usuario)

@router.delete("/usuarios/{id}")
def delete_usuario(id: str):
    usuarioEncontrado = deletarUsuario(id)
    
    if not usuarioEncontrado:
        raise HTTPException(status_code=404, detail=msg)
    return {"msg": "Usuário removido com sucesso."}

@router.patch("/usuarios/{id}")
def patch_usuario(id: str, usuario: UsuarioUpdate):
    usuarioEncontrado = atualizarUsuario(id, usuario.dict(exclude_unset=True))
    
    if not usuarioEncontrado:
        raise HTTPException(status_code=404, detail=msg)
    return usuarioEncontrado