from typing import Optional

from pydantic import BaseModel

class Login(BaseModel):
    user: str
    pwd: str
    user_type: Optional[int] = None

