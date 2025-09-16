from alembic.config import Config
from alembic import command
from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database import engine

from app.web_models import PersonPostRequest, PersonResponse
from app.crud import add_person, retrieve_persons

app = FastAPI(root_path="/api")

@app.get("/persons")
def get_persons(page: int = 0, limit: int = 5, is_archived: bool | None = None) -> list[PersonResponse]:

    session = Session(engine)
    persons = retrieve_persons(session, page, limit, is_archived)

    return [PersonResponse(
        first_name=person.first_name,
        last_name=person.last_name,
        is_archived=person.is_archived,
        date_added=person.date_added)
            for person in persons]


@app.post("/persons", status_code=201)
def post_person(person: PersonPostRequest):
    session = Session(engine)
    try:
        add_person(session, person)
    except:
        print(":(")