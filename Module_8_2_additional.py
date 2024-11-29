def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {item}")

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set, str)):
            raise TypeError("Некорректный тип данных")

        total, incorrect = personal_sum(numbers)

        if len(numbers) - incorrect == 0:
            return 0

        # Возвращаем среднее арифметическое
        return total / (len(numbers) - incorrect)

    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


# Примеры вызова
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка, некорректные типы
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё корректно
