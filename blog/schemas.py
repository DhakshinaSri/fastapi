from typing import List, Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int

class Blog(BlogBase):
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    
    class Config():
        from_attributes = True

class UserBlog(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: UserBlog
    
    class Config():
        from_attributes = True
    
class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None 
