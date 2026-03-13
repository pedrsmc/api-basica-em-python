from models.usuario import UsuarioCreate
from database import database
from fastapi import HTTPException
import uuid
import os

def listarUsuarios():
    conn = database.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()

    conn.close()
    os.system("bash backup_db.sh")
    return [dict(usuario) for usuario in usuarios]
      
def cadastrarUsuario(usuario: UsuarioCreate):
    id = str(uuid.uuid4())
    conn = database.conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO Usuarios (id, nome, email, tel, idade) VALUES (?, ?, ?, ?, ?)",
        (id, usuario.nome, usuario.email, usuario.tel, usuario.idade)
    )
    conn.commit()

    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    
    conn.close()
    os.system("bash backup_db.sh")
    return dict(usuario)

def buscarUsuario(id: str):
    conn = database.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if not usuario:
        conn.close()
        return None

    conn.close()
    os.system("bash backup_db.sh")
    return dict(usuario)

def atualizarUsuario(id: str, dados: dict):
    if not dados:
        raise HTTPException(status_code=400, detail="Nenhum campo enviado para atualização")

    conn = database.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    if not usuario:
        conn.close()
        return None
    
    nome = dados.get("nome", usuario["nome"])
    email = dados.get("email", usuario["email"])
    tel = dados.get("tel", usuario["tel"])
    idade = dados.get("idade", usuario["idade"])

    cursor.execute(
        "UPDATE Usuarios SET nome = ?, email = ?, tel = ?, idade = ? WHERE id = ?",
        (nome, email, tel, idade, id)
    )

    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id,))
    novoUsuario = cursor.fetchone()
    
    conn.commit()
    conn.close()
    os.system("bash backup_db.sh")
    return dict(novoUsuario)

def deletarUsuario(id: str):
    conn = database.conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if not usuario:
        conn.close()
        return None
    
    cursor.execute("DELETE FROM Usuarios WHERE id = ?", (id,))
   
    conn.commit()
    conn.close()
    os.system("bash backup_db.sh")
    return usuario