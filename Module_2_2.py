

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
f = first
s = second
t = third

# Вариант 1

my_set = {f,s,t}

if len(my_set) == 1:
    print('3')
elif len(my_set) == 2:
    print('2')
else:
    print('0')

# Вариант 2

if f == s == t:
    print('3')
elif f == s or s == t or t == f:
    print('2')
else:
    print('0')


