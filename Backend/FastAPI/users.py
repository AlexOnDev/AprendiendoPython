from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel): # Al heredar de basemodel tiene capacidad de crear una entidad gracias al BaseModel
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Alejandro", surname="de Pablo", url="http://wikipedia.com",age=22),
         User(name="Pepe", surname="Perez", url="http://wiki.com",age=22),
         User(name="Haakon", surname="Dahlberg", url="http://haakon.com",age=20)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Alejandro", "apellido":"de Pablo", "url":"http://wikipedia.com", "age":22},
            {"name":"Pepe", "apellido":"Perez", "url":"http://wiki.com", "age":22},
            {"name":"Haakon", "apellido":"Dahlberg", "url":"http://haakon.com", "age":20}]

@app.get("/users")
async def users():
    # return User(name = "Alejandro", surname="de Pablo", url="http://wikipedia.com", age=22)
    return users_list