from fastapi import APIRouter
from fastapi import status
from api.v1.user.model.user_model import User

router = APIRouter()


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
async def update_by_id(user_id: str):
    print("route: update_by_id")
    print("received value:", user_id)
    return User(
        id="xxx",
        password="xxx",
        name="xxx",
        email="xxx@yyy.com"
    )
