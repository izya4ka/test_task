from datetime import datetime

from app.models import PersonWebModel
from app.web_models import PersonPostRequest

from datetime import datetime
from typing import List

memory: List[PersonWebModel] = [
    PersonWebModel(
        id=1,
        first_name="Анна",
        last_name="Иванова",
        is_archived=False,
        date_added=datetime(2023, 5, 12, 14, 30)
    ),
    PersonWebModel(
        id=2,
        first_name="Дмитрий",
        last_name="Петров",
        is_archived=True,
        date_added=datetime(2022, 8, 3, 9, 15)
    ),
    PersonWebModel(
        id=3,
        first_name="Елена",
        last_name="Сидорова",
        is_archived=False,
        date_added=datetime(2024, 1, 20, 11, 45)
    ),
    PersonWebModel(
        id=4,
        first_name="Михаил",
        last_name="Козлов",
        is_archived=False,
        date_added=datetime(2023, 11, 7, 16, 20)
    ),
    PersonWebModel(
        id=5,
        first_name="Ольга",
        last_name="Морозова",
        is_archived=True,
        date_added=datetime(2021, 12, 15, 10, 5)
    ),
    PersonWebModel(
        id=6,
        first_name="Алексей",
        last_name="Федоров",
        is_archived=False,
        date_added=datetime(2024, 3, 25, 13, 35)
    ),
    PersonWebModel(
        id=7,
        first_name="Наталья",
        last_name="Волкова",
        is_archived=False,
        date_added=datetime(2023, 7, 18, 17, 10)
    ),
    PersonWebModel(
        id=8,
        first_name="Сергей",
        last_name="Алексеев",
        is_archived=False,
        date_added=datetime(2024, 2, 14, 8, 50)
    ),
    PersonWebModel(
        id=9,
        first_name="Татьяна",
        last_name="Лебедева",
        is_archived=True,
        date_added=datetime(2022, 4, 30, 12, 25)
    ),
    PersonWebModel(
        id=10,
        first_name="Игорь",
        last_name="Семёнов",
        is_archived=False,
        date_added=datetime(2023, 9, 5, 15, 40)
    ),
    PersonWebModel(
        id=11,
        first_name="Мария",
        last_name="Степанова",
        is_archived=False,
        date_added=datetime(2024, 4, 10, 10, 20)
    ),
    PersonWebModel(
        id=12,
        first_name="Владимир",
        last_name="Николаев",
        is_archived=False,
        date_added=datetime(2023, 6, 22, 14, 10)
    ),
    PersonWebModel(
        id=13,
        first_name="Юлия",
        last_name="Орлова",
        is_archived=True,
        date_added=datetime(2021, 10, 8, 16, 30)
    ),
    PersonWebModel(
        id=14,
        first_name="Павел",
        last_name="Макаров",
        is_archived=False,
        date_added=datetime(2024, 1, 3, 11, 55)
    ),
    PersonWebModel(
        id=15,
        first_name="Ксения",
        last_name="Андреева",
        is_archived=False,
        date_added=datetime(2023, 12, 19, 13, 15)
    ),
    PersonWebModel(
        id=16,
        first_name="Роман",
        last_name="Васильев",
        is_archived=False,
        date_added=datetime(2024, 5, 2, 9, 40)
    ),
    PersonWebModel(
        id=17,
        first_name="Алёна",
        last_name="Григорьева",
        is_archived=True,
        date_added=datetime(2022, 7, 14, 10, 30)
    ),
    PersonWebModel(
        id=18,
        first_name="Борис",
        last_name="Зайцев",
        is_archived=False,
        date_added=datetime(2023, 10, 28, 12, 10)
    ),
    PersonWebModel(
        id=19,
        first_name="Виктория",
        last_name="Кузнецова",
        is_archived=False,
        date_added=datetime(2024, 3, 11, 14, 0)
    ),
]

def paginate_list(
    page: int,
    limit: int,
    show_archived: bool | None = None
) -> dict:

    if show_archived is None:
        filtered_items = [item for item in memory if not item.is_archived]
    else:
        filtered_items = memory
    
    total = len(filtered_items)

    start_index = (page - 1) * limit
    end_index = start_index + limit

    paginated_items = filtered_items[start_index:end_index]

    return {
        "items": paginated_items,
        "total": total
    }
    
def add_person_to_memory(person_data: PersonPostRequest):

    id = memory[-1].id
    
    new_person = PersonWebModel(
        id= 0 if id is None else (id+1),
        first_name=person_data.first_name,
        last_name=person_data.last_name,
        is_archived=person_data.is_archived,
        date_added=datetime.now()
    )

    memory.append(new_person)