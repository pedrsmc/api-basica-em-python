from models.usuario import UsuarioCreate
from database import database
from psycopg2.extras import RealDictCursor
import uuid

def listarUsuarios():
    conn = database.conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()

    conn.close()
    return [dict(usuario) for usuario in usuarios]
      
def cadastrarUsuario(usuario: UsuarioCreate):
    id = str(uuid.uuid4())
    conn = database.conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        "INSERT INTO Usuarios (id, nome, email, tel, idade) VALUES (%s, %s, %s, %s, %s)",
        (id, usuario.nome, usuario.email, usuario.tel, usuario.idade)
    )
    conn.commit()

    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    usuario_db = cursor.fetchone()
    
    conn.close()
    return dict(usuario_db)

def buscarUsuario(id: str):
    conn = database.conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()

    conn.close()
    return dict(usuario) if usuario else None

def atualizarUsuario(id: str, dados: dict):
    conn = database.conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    
    if not usuario:
        conn.close()
        return None
    
    nome = dados.get("nome", usuario["nome"])
    email = dados.get("email", usuario["email"])
    tel = dados.get("tel", usuario["tel"])
    idade = dados.get("idade", usuario["idade"])

    cursor.execute(
        "UPDATE Usuarios SET nome = %s, email = %s, tel = %s, idade = %s WHERE id = %s",
        (nome, email, tel, idade, id)
    )
    conn.commit()

    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    novoUsuario = cursor.fetchone()

    conn.close()
    return dict(novoUsuario)

def deletarUsuario(id: str):
    conn = database.conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()

    if not usuario:
        conn.close()
        return None
    
    cursor.execute("DELETE FROM Usuarios WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    
    return dict(usuario)