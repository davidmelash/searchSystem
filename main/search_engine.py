from django.db.models import Q

from main.models import Profile
from datetime import datetime

FORMAT = "%Y-%m-%d"

filter_mapper = {
    "Початок з": "__startswith",
    "Кінець з": "__endswith",
    "Повний збіг": "",
    "Частковий збіг": "__icontains",
}


def build_query(filter_type: str, entity_type: str, value: str) -> dict:
    fields_model_mapper = {
        "Номер Телефону": {f"phone_number{filter_type}": value},
        "П.І.Б": {f"full_name{filter_type}": value},
        "Дата Народження": {f"data_of_birth{filter_type}": value},
        "ІПН": {f"identification_number{filter_type}": value},
        "Адреса": {f"address{filter_type}": value},
        "Коментар": {f"comments{filter_type}": value}
    }
    return fields_model_mapper.get(entity_type)


def check_date_format(date: str) -> bool:
    try:
        result = bool(datetime.strptime(date, FORMAT))
    except ValueError:
        result = False
    return result


def make_search(filter_type: str, entity_type: str, value: str):
    if entity_type == "Довільний текст":
        result = Profile.objects.filter(
            Q(phone_number__icontains=value) |
            Q(data_of_birth__icontains=value) |
            Q(identification_number__icontains=value) |
            Q(address__icontains=value) |
            Q(comments__icontains=value) |
            Q(full_name__icontains=value)).values()
    else:
        query_filter = filter_mapper.get(filter_type)
        query = build_query(query_filter, entity_type, value)
        result = Profile.objects.filter(**query).values()
    return result
