from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

class AuthorBase(BaseModel):
    name: str
    biography: str

class AuthorCreate(AuthorBase):
    pass

class AuthorOut(AuthorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookBase(BaseModel):
    title: str
    description: str
    rating: float
    author_id: int

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None
