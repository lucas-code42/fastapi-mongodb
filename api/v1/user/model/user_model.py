from pydantic import BaseModel, validator
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    password: str

    @validator("name")
    def validate_id(cls, value: str) -> str:
        if not value.isalpha():
            raise ValueError("name can just contain alphabet letters")
        return value

    @validator("email")
    def validate_email(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError("email is not valid")
        return value

    # @validator("password")
    # def validate_id(cls, value: str) -> str:
    #     if ["@", ".", "com"] not in value:
    #         raise ValueError("email is not valid")
    #     return value
