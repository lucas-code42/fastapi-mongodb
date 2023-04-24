from api.v1.database.api_mongo_db import mongo_connect_client
from pymongo import MongoClient
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from api.v1.user.model.user_model import User
from bson.raw_bson import RawBSONDocument
from bson import encode


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def create(user: User, mongo_client: MongoClient=Depends(mongo_connect_client)):
    try:
        user.id = str(uuid4())
        db = mongo_client.test # set database
        collection = db.users # set collection
        collection.insert_one(RawBSONDocument(encode(user.dict()))) # set dict to bson
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="data doesn't match"
        )
    finally:
        mongo_client.close()
    return user
