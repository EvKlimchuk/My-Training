class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return 'Building name: self.name, number of floors: self.number_of_floors'

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

# __str__
print(h3)
print(h4)

# __len__
print(len(h3))
print(len(h4))
