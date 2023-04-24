from fastapi import APIRouter, HTTPException, Depends
from fastapi import status
from api.v1.database.api_mongo_db import mongo_connect_client
from api.v1.user.model.user_model import User
from pymongo import MongoClient

router = APIRouter()


@router.post("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
async def update_by_id(user: User, user_id: str, mongo_client: MongoClient = Depends(mongo_connect_client)):
    try:
        db = mongo_client.test  # set database
        collection = db.users  # set collection
        query = {"id": user_id}
        for usr in collection.find(query):
            mongo_user = usr
        update = {
            "$set":
            {
                "name": user.name, 
                "email": user.email,
                "password": user.password
            }
        }
        update_result = collection.update_one(filter=mongo_user, update=update)
        # {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
        if update_result.raw_result["n"] != 1 and update_result.raw_result["nModified"] != 1 and not update_result.raw_result["updatedExisting"]:
            raise AttributeError
    except AttributeError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="check the send data"
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error"
        )
    finally:
        mongo_client.close()

    return user
