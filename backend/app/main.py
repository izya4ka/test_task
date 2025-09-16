from os import environ
from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database import engine

from app.web_models import PersonPostRequest, PersonListResponse, PersonWebModel
from app.crud import add_person, retrieve_persons
from app.memory import paginate_list, memory, add_person_to_memory

app = FastAPI(root_path="/api")

use_memory = environ["USE_MEMORY"]

@app.get("/persons", response_model=PersonListResponse)
def get_persons(page: int = 1, limit: int = 5, show_archived: bool | None = None):
    if use_memory != "":
        return paginate_list(page, limit, show_archived)
    try:
        session = Session(engine)
        persons, total = retrieve_persons(session, page-1, limit, show_archived)
        
        return {
            "items": [PersonWebModel(
            id=person.id,
            first_name=person.first_name,
            last_name=person.last_name,
            is_archived=person.is_archived,
            date_added=person.date_added)
                for person in persons],
            "total": total
        }
    except:
        print(":(")
    finally:
        session.close()


@app.post("/persons", status_code=201)
def post_person(person: PersonPostRequest):
    if use_memory != "":
        add_person_to_memory(person)
        return
        
    session = Session(engine)
    try:
        add_person(session, person)
    except:
        print(":(")
    finally:
        session.close()