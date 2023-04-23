from fastapi import APIRouter
from fastapi import status
from api.v1.user.model.user_model import User
from typing import List
from api.v1.database.api_mongo_db import mongo_connect_client
from fastapi import Depends
from pymongo import MongoClient

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[User])
async def read_all(db: MongoClient = Depends(mongo_connect_client)):
    print("route: read_all")
    print(db.test)
    print(db.my_collection)

    return [
        User(
            id="xxx",
            password="xxx",
            name="xxx",
            email="xxx@yyy.com"
        ),
        User(
            id="www",
            password="www",
            name="www",
            email="www@yyy.com"
        )
    ]


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
async def read_by_id(user_id: str):
    print("route: read_by_id")
    print("received value:", user_id)
    return User(
        id="xxx",
        password="xxx",
        name="xxx",
        email="xxx@yyy.com"
    )
