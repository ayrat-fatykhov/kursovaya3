import json


def get_operations() -> list[dict]:
    """
    Форматирует json в python
    :return: список операций
    """
    with open('operations.json', encoding='utf-8') as file:
        return json.load(file)
