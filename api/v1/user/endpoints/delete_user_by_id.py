from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from api.v1.database.api_mongo_db import mongo_connect_client
from pymongo import MongoClient
from api.v1.user.model.user_model import User
from typing import Optional


router = APIRouter()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: str, mongo_client: MongoClient = Depends(mongo_connect_client)):
    user: Optional[User] = None
    try:
        db = mongo_client.test
        collection = db.users
        query = {"id": user_id}
        result = collection.delete_one(query)
        # print(result.raw_result)
        # check the metadata result of delete {'n': 0, 'ok': 1.0}
        if result.raw_result["n"] != 1:
            raise NameError("nothing to delete")
        print(type(result))
    except NameError as err:
        print(err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="nothing to delete"
        )
    except Exception as e:  # Exception is the lowest level so need to be de last
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="server error"
        )
    finally:
        mongo_client.close()

    return user
