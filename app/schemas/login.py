from pydantic import BaseModel

class Login(BaseModel):
    user: str
    pwd: str
    user_type: int

