from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user
class User(BaseModel): # Al heredar de basemodel tiene capacidad de crear una entidad gracias al BaseModel
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Alejandro", surname="de Pablo", url="http://wikipedia.com",age=22),
         User(id=2,name="Pepe", surname="Perez", url="http://wiki.com",age=22),
         User(id=3,name="Haakon", surname="Dahlberg", url="http://haakon.com",age=20)]

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Alejandro", "apellido":"de Pablo", "url":"http://wikipedia.com", "age":22},
            {"name":"Pepe", "apellido":"Perez", "url":"http://wiki.com", "age":22},
            {"name":"Haakon", "apellido":"Dahlberg", "url":"http://haakon.com", "age":20}]

@app.get("/users")
async def users():
    # return User(name = "Alejandro", surname="de Pablo", url="http://wikipedia.com", age=22)
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int): # FastApi trabaja tipando los datos
    return search_user(id)
    
# Query
@app.get("/user/") # http://127.0.0.1:8000/userquery/?id=1 (query)
async def user(id: int): # FastApi trabaja tipando los datos
    return search_user(id)
    


def search_user(id: int):
    users = filter(lambda user: user.id ==id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}