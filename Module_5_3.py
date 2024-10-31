class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Building name: {self.name}, number of floors: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)



h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)


print(h3)
print(h4)


print(h3 == h4) # __eq__

h3 == h3 + 10 # __add__
print(h3)
print(h3 == h4)

h3 += 10 # __add__
print(h3)

h4 = 10 + h4 #__radd
print(h4)

print(h3 < h4)
print(h3 <= h4)
print(h3 > h4)
print(h3 >= h4)
print(h3 != h4)