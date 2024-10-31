# Домашнее задание по Модулю 5.1 Задача "Developer - не только разработчик"

class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to_floor(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(new_floor):
                print(floor + 1)
        else:
            print("This floor doesn't exist")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to_floor(5)
h2.go_to_floor(10)