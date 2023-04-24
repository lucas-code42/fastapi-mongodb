from fastapi import APIRouter
from fastapi import status, HTTPException
from api.v1.user.model.user_model import User
from typing import List
from api.v1.database.api_mongo_db import mongo_connect_client
from fastapi import Depends
from pymongo import MongoClient

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[User])
async def read_all(mongo_client: MongoClient = Depends(mongo_connect_client)):
    users: List[User] = []
    try:
        db = mongo_client.test  # set database
        collection = db.users  # set collection
        for usr in collection.find():  # find() return's a cursor
            # print(usr) {'_id': ObjectId('6445c9793a8d26185fe4b170'), 'id': '9dd70c28-670f-44b7-9a23-67ce1ac44b3b', 'name': 'test', 'email': 'test@test.com', 'password': 'test1'}
            # print(type(usr)) dict
            users.append(usr)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error"
        )
    finally:
        mongo_client.close()

    return users


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
async def read_by_id(user_id: str, mongo_client: MongoClient = Depends(mongo_connect_client)):
    user: User
    try:
        db = mongo_client.test
        collection = db.users
        query = {"id": user_id}
        for usr in collection.find(query):
            user = usr
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error"
        )
    finally:
        mongo_client.close()

    return user
