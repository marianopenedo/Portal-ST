from typing import Optional

from pydantic import BaseModel, ConfigDict


class CompanySchema(BaseModel):
    id: Optional[int] = None
    service_type: str
    name: str
    identity: str
    social_name: str
    profile: str
    status: str
    direct_invoicing: bool
    
    user_type: Optional[str] = None
    path_file: Optional[str] = None
    reproval_message: Optional[str] = None
