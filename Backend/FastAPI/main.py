from fastapi import FastAPI
from routers import products, users

# python -m uvicorn main:app --reload
app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return "¡Hola FastApi!"

@app.get("/url")
async def url():
    return { "url":"https://cursos.com" }

# Documentación con Swagger: http://127.0.0.:8000/docs
# Documentación con Redocly: http://127.0.0.:8000/redoc