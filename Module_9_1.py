def apply_all_func(int_list, *functions):

    results = {}

    for func in functions:
        try:
            # Применение функции к списку и сохранение результата в словарь
            results[func.__name__] = func(int_list)
        except Exception as e:
            # Если функция вызвала ошибку, записываем сообщение об ошибке
            results[func.__name__] = f"Ошибка: {e}"

    return results

# Примеры функций и вызовов
print(apply_all_func([6, 20, 15, 9], max, min))  # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
