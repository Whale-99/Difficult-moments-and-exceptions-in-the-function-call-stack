# Функция personal_sum, которая подсчитывает сумму чисел и количество некорректных данных
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1
    return result, incorrect_data


# Функция calculate_average, которая вычисляет среднее значение
def calculate_average(numbers):
    try:
        # Проверка на пустую коллекцию
        total_sum, incorrect_data = personal_sum(numbers)
        valid_count = len(numbers) - incorrect_data

        # Проверка на деление на 0
        return total_sum / valid_count if valid_count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
