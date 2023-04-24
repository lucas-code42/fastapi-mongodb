import pymongo
from pymongo import MongoClient
from api.api_settings import api_settings


async def mongo_connect_client() -> MongoClient:
    client = pymongo.MongoClient(host=api_settings.DB_HOST)
    try:
        yield client
    finally:
        client.close()
