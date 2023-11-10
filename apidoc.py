from pydantic import BaseModel


# post
class getscore(BaseModel):
    studentid: str


# get resp
class generalresp(BaseModel):
    httpcode: int
    msg: str
    timestamp: int
    data: list
