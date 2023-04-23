from fastapi import APIRouter
from fastapi import status
from api.v1.user.model.user_model import User

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def create(user: User):
    print("route: create")
    print("received value", user)
    return User(
            id="xxx",
            password="xxx",
            name="xxx",
            email="xxx@yyy.com"
    )
