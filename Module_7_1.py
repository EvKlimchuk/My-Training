
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_str =file.read()
        file.close()
        return prod_str

    def add(self, *products):
        existing_products = self.get_products()
        for product in products:
            if str(product)in existing_products:
                print(f"Продукт {product} уже есть в магазине")
            else:
                _file = open(self.__file_name, 'a')
                _file.write(f'{str(product)}\n')
                _file.close()


# Создаём экземпляры магазина и продуктов
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Проверяем вывод метода __str__
print(p2)  # Вывод: Spaghetti, 3.4, Groceries

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем список всех продуктов
print(s1.get_products())
