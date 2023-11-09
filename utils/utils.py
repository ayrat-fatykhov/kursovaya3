def sort_only_dates(operations) -> list:
    """
    Создает список с датами и сортирует его
    :param operations: операции
    :return: сортированные даты
    """
    all_dates: list = []
    for operation in operations:
        for key in operation:
            if key == 'date':
                all_dates.append(operation['date'])
    sort_date: list = sorted(all_dates, reverse=True)
    return sort_date


def sort_by_date(operations) -> list[dict]:
    """
    Сортирует операции по датам
    :param operations: операции
    :return: сортированные по датам операции
    """
    sort_operations: list = []
    sort_date: list = sort_only_dates(operations)
    for i in range(len(sort_date)):
        for operation in operations:

            for key in operation:
                if key == 'date':
                    if sort_date[i] in operation[key]:
                        sort_operations.append(operation)
    return sort_operations


def get_reformat_dates(operations) -> list[dict]:
    """
    Приводит даты в формат ДД.ММ.ГГГГ
    :param operations: операции
    :return: операции с измененным форматом дат
    """
    reformat_dates: list[dict] = sort_by_date(operations)
    for operation in reformat_dates:
        for key in operation:
            if key == 'date':
                old_data: str = operation[key]
                slice_data: str = old_data[0:10]
                split_data: list = slice_data.split("-")
                rev_data = reversed(split_data)
                new_data: str = ".".join(rev_data)
                operation[key] = new_data
    return reformat_dates


def get_reform_numbers(operations) -> list[dict]:
    """
    Скрывает часть номера счета и карты
    :param operations: операции
    :return: операции со скрытыми номерами счетов и карт
    """
    reform_number: list[dict] = get_reformat_dates(operations)
    key1: str = 'from'
    key2: str = 'to'
    for i in range(2):
        for operation in reform_number:
            for key in operation:
                if key == key1:
                    if 'Счет' in operation[key1]:
                        old_number: str = operation[key1] + ' '
                        slice_number: str = old_number[-5:-1]
                        new_number: str = 'Счет **' + slice_number
                        operation[key] = new_number
                    else:
                        old_number: str = operation[key1] + ' '
                        slice_number_one: str = old_number[0:-13]
                        slice_number_two: str = old_number[-13:-11]
                        slice_number_free: str = old_number[-5:-1]
                        new_number: str = slice_number_one + ' ' + slice_number_two + '** **** ' + slice_number_free
                        operation[key] = new_number
        key1 = key2
    return reform_number


def get_executed(operations):
    """
    Выбирает только прошедшие операции
    :param operations: операции
    :return: пройденные операции
    """
    executed_operations: list = []
    sort_operations: list[dict] = get_reform_numbers(operations)
    for operation in sort_operations:
        for key in operation:
            if key == 'state':
                if operation['state'] == 'EXECUTED':
                    executed_operations.append(operation)
    return executed_operations
