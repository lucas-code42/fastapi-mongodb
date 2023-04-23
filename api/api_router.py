from fastapi import APIRouter

from api.v1.user.endpoints import create_user
from api.v1.user.endpoints import delete_user_by_id
from api.v1.user.endpoints import read_user
from api.v1.user.endpoints import update_user

user_endpoints = APIRouter()
user_endpoints.include_router(create_user.router, prefix="/create", tags=["create_user"])
user_endpoints.include_router(delete_user_by_id.router, prefix="/delete", tags=["delete_user"])
user_endpoints.include_router(read_user.router, prefix="/read", tags=["read_user"])
user_endpoints.include_router(update_user.router, prefix="/update", tags=["update_user"])
