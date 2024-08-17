from pydantic import BaseModel
from typing import Optional

# Entidad user
class User(BaseModel):
    # id: str | None  # String porque mongo los crea string para crear id unicos mas facil
    id: Optional [str] = None # Error 422
    username: str
    email: str