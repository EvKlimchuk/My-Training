# Домашнее задание по уроку "Распоковка позиционных параметров".

# Задача "Распаковка"
#
# Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:

value_list = ['Module', 3, True]
value_dict = {'a': 'Module', 'b': 4, 'c' : False}

print_params(*value_list)
print_params(**value_dict)

value_list2 = [54.32, 'String']
print_params(*value_list2, 42)