# Данные
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, длина которых >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список пар (кортежей) слов одинаковой длины из обоих списков
second_result = [
    (f, s)
    for f in first_strings
    for s in second_strings
    if len(f) == len(s)
]

# 3. Словарь из объединённых списков строк: ключ — строка, значение — её длина (условие: длина строки чётная)
third_result = {
    s: len(s)
    for s in first_strings + second_strings
    if len(s) % 2 == 0
}


print(first_result)
print(second_result)
print(third_result)
