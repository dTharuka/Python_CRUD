from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    firstName: str
    lastName: str
    userName: str
    email: str
    contactNumber: str
    gender: str
    country: str
    state: str
    city: str