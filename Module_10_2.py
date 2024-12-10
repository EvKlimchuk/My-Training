import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.total_enemies = 100  # Каждый рыцарь сражается со 100 воинами

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")

        while self.total_enemies > 0:
            days += 1
            self.total_enemies -= self.power
            self.total_enemies = max(self.total_enemies, 0)  # Не допускаем отрицательного количества
            print(f"{self.name}, сражается {days} день(дня)..., осталось {self.total_enemies} воинов.")
            time.sleep(1)  # Задержка в 1 секунду

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Финальная строка
print("Все битвы закончились!")
