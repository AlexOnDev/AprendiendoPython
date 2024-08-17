from fastapi import APIRouter, HTTPException, status
import logging
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId 

router = APIRouter(prefix="/userdb", 
                   tags=["userdb"], 
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}}) 

users_list = []

# python -m uvicorn main:app --log-level debug
logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


@router.get("/", response_model=list[User]) # Valida FastApi y ademas lo mete en la docu
async def users():
    return users_schema(db_client.local.users.find())

# Path
@router.get("/{id}")
async def user(id: str): 
    return search_user("_id", ObjectId(id)) #Oid como el que tiene mongodb en cada elemento
    
# Query
@router.get("/") 
async def user(id: str):
    return search_user("_id", ObjectId(id))

# Post  
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    
    user_dict = dict(user)
    # logger.debug(user_dict)
    del user_dict["id"] # Asi mongoDB autogenera el id

    id = db_client.local.users.insert_one(user_dict).inserted_id # MongoDB funciona con JSON
    new_user = user_schema(db_client.local.users.find_one({"_id":id})) # _id  # (formato JSON)
    # logger.debug(new_user)
    
    
    return User(**new_user)

# Put     
@router.put("/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
         return {"error":"No se ha actualizado el usuario"}
    
    return user

# Delete
@router.delete("/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list): 
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
         return {"error":"No se ha eliminado el usuario"}


def search_user(field: str, key):
    try:
        user = user_schema(db_client.local.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error":"No se ha encontrado el usuario"}