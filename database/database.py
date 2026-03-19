import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def conectar():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        return conn
    except Exception as erro:
        print("Erro ao tentar se conectar ao banco: ", erro)
        return None