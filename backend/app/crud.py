import datetime
from typing import Tuple

from sqlalchemy import func, select
from app.database import engine
from sqlalchemy.orm import Session
from app.models import PersonWebModel
from app.web_models import PersonPostRequest

def retrieve_persons(session: Session, page: int, limit: int, show_archived: bool | None) -> Tuple[list[PersonWebModel], int]:
    stmt = select(PersonWebModel)

    if (show_archived == False) or (show_archived == None):
        stmt = stmt.where(PersonWebModel.is_archived == False)

    count_stmt = select(func.count()).select_from(stmt.subquery())
    
    stmt = stmt.offset(page * limit).limit(limit)
    
    count = session.scalar(count_stmt)
    
    return (list(session.scalars(stmt).all()), 0 if count is None else count)

def add_person(session: Session, person: PersonPostRequest):

    db_person = PersonWebModel(
        first_name=person.first_name,
        last_name=person.last_name,
        is_archived=person.is_archived,
        date_added=datetime.datetime.now()
    )
    
    session.add(db_person)
    session.commit()