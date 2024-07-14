filter_mapper = {
    "Початок з": "__startswith",
    "Кінець з": "__endswith",
    "Повний збіг": "",
    "Частковий збіг": "contains",
}

print(filter_mapper.get("Частковий збіг"))