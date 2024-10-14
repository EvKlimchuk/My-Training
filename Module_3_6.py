# Дополнительное практическое задание по модулю 3: "Подробнее о функциях"
# Задание "Раз, два, три, четыре, пять .... Это не все?"

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
   total_sum = 0
   for item in data:
      if isinstance(item, list) or isinstance(item, set) or isinstance(item, tuple):
         total_sum += calculate_structure_sum(item)
      elif isinstance(item, dict):
         a, b = item.keys(), item.values()
         total_sum += calculate_structure_sum(a)
         total_sum += calculate_structure_sum(b)
      elif isinstance (item, int):
         total_sum += item
      elif isinstance (item, str):
         total_sum += len(item)
   return total_sum

result = calculate_structure_sum(data_structure)
print(result)




