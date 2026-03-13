from fastapi import FastAPI
from routers import usuario_routers
import uvicorn
import os

app = FastAPI()
app.include_router(usuario_routers.router)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)