# Расчет среднеарифметического значения каждого элемента
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
av_grades = [sum(x)/len(x) for x in grades]

# Конвертация множества ключей в лист и сортировка ключей в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
list_students.sort()

# Создание словаря
d = dict(zip(list_students, av_grades))
print(d)
