def is_prime(func):
    """Декоратор для проверки, является ли результат функции простым числом."""
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        # Проверяем, является ли результат простым числом
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное число")
                    break
            else:
                print("Простое число")
        else:
            print("Результат является отрицательным числом или 0 или 1")

        # Возвращаем результат функции
        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    """Функция для сложения трёх чисел."""
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)

