# API de Usuários

API REST simples para gerenciamento de usuários feita com **FastAPI** e **PostgreSQL**.

## Tecnologias

* Python
* FastAPI
* PostgreSQL
* Uvicorn

## Executar localmente

Instalar dependências:

```
pip install -r requirements.txt
```

Rodar a API:

```
uvicorn main:app --reload
```

Acesse a documentação automática:

```
http://localhost:8000/docs
```

## Endpoints

```
GET    /usuarios
GET    /usuarios/{id}
POST   /usuarios
PUT    /usuarios/{id}
DELETE /usuarios/{id}
```

## Docs

https://api-basica-em-python.onrender.com/docs
