import datetime
from pydantic import BaseModel


class PersonPostRequest(BaseModel):
    first_name: str
    last_name: str
    is_archived: bool

class PersonResponse(BaseModel):
    first_name: str
    last_name: str
    is_archived: bool
    date_added: datetime.datetime