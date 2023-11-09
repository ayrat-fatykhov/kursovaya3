from data import get_operations
from utils.utils import get_executed, sort_by_date

data: list[dict] = get_operations()


def get_conclusion(operations) -> None:
    """
    Выводит последние 5 операций
    :param operations: список операций
    :return: нечего
    """
    all_operations: list[dict] = get_executed(operations)
    for i in range(5):
        if 'from' in all_operations[i]:
            print(f"""{all_operations[i]['date']} {all_operations[i]['description']}
            \r{all_operations[i]['from']} -> {all_operations[i]['to']}
            \r{all_operations[i]['operationAmount']['amount']} {all_operations[i]['operationAmount']['currency']['name']}
            """)
        else:
            print(f"""{all_operations[i]['date']} {all_operations[i]['description']}
            \r{all_operations[i]['to']}
            \r{all_operations[i]['operationAmount']['amount']} {all_operations[i]['operationAmount']['currency']['name']}
            """)


if __name__ == '__main__':
    get_conclusion(data)
