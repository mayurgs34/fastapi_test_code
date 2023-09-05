from pydantic import BaseModel
from typing import Optional

class signUp(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class tokenData(BaseModel):
    email: str
