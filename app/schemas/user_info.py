from typing import Optional

from pydantic import BaseModel

class UserInfo(BaseModel):
    user: str
    pwd: str
    permission: Optional[str] = None 

