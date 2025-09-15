import datetime

from sqlalchemy import select
from app.database import engine
from sqlalchemy.orm import Session
from app.models import Person
from app.web_models import PersonPostRequest, PersonResponse

def retrieve_persons(session: Session, page: int, limit: int, is_archived: bool | None) -> list[Person]:
    stmt = select(Person)

    if (is_archived == False) or (is_archived == None):
        stmt = stmt.where(Person.is_archived == False)

    stmt = stmt.offset(page * limit).limit(limit)
    
    return list(session.scalars(stmt).all())

def add_person(session: Session, person: PersonPostRequest):

    db_person = Person(
        first_name=person.first_name,
        last_name=person.last_name,
        is_archived=person.is_archived,
        date_added=datetime.datetime.now()
    )
    
    session.add(db_person)
    session.commit()