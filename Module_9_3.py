
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка с использованием zip
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))   # [1, 2]
print(list(second_result))  # [False, False, True]
