class StepValueError(ValueError):
    """Класс исключения для неверного шага итерации."""
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start  # Сброс pointer к началу
        return self

    def __next__(self):

        # Проверка на окончание итерации
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current

# Пример использования
try:
    iter1 = Iterator(100, 200, 0)  # Пример с ошибкой
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print("Шаг указан не верно")

iter2 = Iterator(-5, 1)            # Шаг по умолчанию = 1
iter3 = Iterator(6, 15, 2)         # Шаг = 2
iter4 = Iterator(5, 1, -1)         # Отрицательный шаг
iter5 = Iterator(10, 1)        # шаг по умолчанию = 1, значение stop не включается

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
