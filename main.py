from fastapi import FastAPI
from routers import usuario_routers
import os
import requests

app = FastAPI()
app.include_router(usuario_routers.router)

DB_PATH = "database/database.db"

URL_DB = "https://raw.githubusercontent.com/pedrsmc/api-basica-em-python/master/database/database.db"

if not os.path.exists(DB_PATH):
    r = requests.get(URL_DB)
    os.makedirs("database", exist_ok=True)
    open(DB_PATH, "wb").write(r.content)