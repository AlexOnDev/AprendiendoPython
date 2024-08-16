from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastApi!"

@app.get("/url")
async def url():
    return { "url":"https://cursos.com" }

# Documentación con Swagger: http://127.0.0.:8000/docs
# Documentación con Redocly: http://127.0.0.:8000/redoc