from fastapi import APIRouter
from fastapi import status

router = APIRouter()


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: str):
    print("route: delete")
    print("received value:", user_id)
    return
