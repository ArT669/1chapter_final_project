import datetime
from pydantic import BaseModel

class UserGet(BaseModel):
    """Модель pydantic для user"""
    id : int
    age : int
    exp_group : int
    gender : int
    city : str
    country : str
    os : str
    source : str

    class Config():
        orm_mode = True

class PostGet(BaseModel):
    """Модель pydantic для post"""
    id : int
    text : str
    topic : str

    class Config():
        orm_mode = True

class FeedGet(BaseModel):
    """Модель pydantic для feed_action"""
    user_id : int
    post_id : int
    time : datetime.datetime
    action : str
    user : UserGet
    post : PostGet
    
    class Config():
        orm_mode = True