from pydantic import BaseModel, EmailStr

class ContactRequest(BaseModel):
    site: str
    name: str
    email: EmailStr
    message: str
    