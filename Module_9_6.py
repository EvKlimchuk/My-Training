def all_variants(text):
    """Функция-генератор для получения всех подпоследовательностей строки text."""
    n = len(text)
    for length in range(1, n + 1):  # Начало перебора длин подпоследовательности
        for start in range(n - length + 1):  # начальная позиция
            yield text[start:start + length]

# Пример вызова
a = all_variants("abc")
for i in a:
    print(i)

"""Логика:
1. range(1, n + 1) - перебор длины подпоследовательностей:
    (a) Перебираем возможные длины подпоследовательностей от 1 до n включительно.
    (b) Например, для строки "abc":
        length = 1: подпоследовательности длиной 1.
        length = 2: подпоследовательности длиной 2.
        length = 3: подпоследовательности длиной 3.
2. range(n - length + 1) - перебор начальной позиции подпоследовательности:

    (a) Для текущей длины (length) генерируем все возможные начальные позиции (start) в строке.
    (b) start может варьироваться от 0 до n - length.
    (c) Например, для строки "abc":
        Если length = 1: начальные позиции start = 0, 1, 2.
        Если length = 2: начальные позиции start = 0, 1.
        Если length = 3: начальная позиция start = 0.
3. text[start:start + length]:

        Берём срез строки от позиции start до start + length.
        Это формирует подпоследовательность указанной длины."""