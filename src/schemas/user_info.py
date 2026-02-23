from typing import Optional

from pydantic import BaseModel, model_validator

class UserSchema(BaseModel):
    login: str
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    email: str
    user_type: str
    password: Optional[str] = None

    @model_validator(mode='after')
    def check_cpf_cnpj(self):
        if not self.cnpj and not self.cpf:
            raise ValueError()

        return self
