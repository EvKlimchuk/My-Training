import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        if self.__is_valid_color(*color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return all(isinstance(val, int) and 0 <= val <= 255 for val in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side >0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super(). __init__(color, *sides)


    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0]/(2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1 or not isinstance(sides[0], int) or sides[0] <=0:
            sides = [1]
        else:
            sides = [sides[0]] * 12
        super(). __init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] >0:
            sides = [new_sides[0]] * 12
            super().set_sides(*sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


# Код для проверки
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

