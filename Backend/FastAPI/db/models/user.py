from pydantic import BaseModel

# Entidad user
class User(BaseModel):
    id: str | None # String porque mongo los crea string para crear id unicos mas facil
    username: str
    email: str