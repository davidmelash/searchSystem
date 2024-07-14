from main.models import Profile
from datetime import datetime

FORMAT = "%Y-%m-%d"

filter_mapper = {
    "Початок з": "__startswith",
    "Кінець з": "__endswith",
    "Повний збіг": "",
    "Частковий збіг": "__contains",
}


def build_query(filter_type: str, entity_type: str, value: str) -> dict:
    fields_model_mapper = {
        "Номер Телефону": {f"phone_number{filter_type}": value},
        "П.І.Б": {f"full_name{filter_type}": value},
        "Дата Народження": {f"data_of_birth{filter_type}": value},
        "ІПН": {f"identification_number{filter_type}": value}
    }
    print(f"{filter_type}|{entity_type}|{value}|3")
    return fields_model_mapper.get(entity_type)


def check_date_format(date: str) -> bool:
    try:
        result = bool(datetime.strptime(date, FORMAT))
    except ValueError:
        result = False
    return result



def make_search(filter_type: str, entity_type: str, value: str):
    if filter_type == "Повний збіг" and entity_type == "Дата Народження" and not check_date_format(value):
        return
    query_filter = filter_mapper.get(filter_type)
    print(f"{filter_type}|{entity_type}|{value}|2")
    query = build_query(query_filter, entity_type, value)
    print(query, "QUERYYY")
    result = Profile.objects.filter(**query).values()
    print(result, "RESULT")
    return result