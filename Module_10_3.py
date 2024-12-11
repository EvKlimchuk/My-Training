import threading
import random
import time

balance = 0

class Bank:
    def __init__(self):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):

        for _ in range(100):
            amount = random.randint(50, 500)  # Случайное пополнение
            self.lock.acquire()
            try:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            finally:
                if self.lock.locked():
                    self.lock.release()

            time.sleep(0.001)  # Задержка

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайное снятие
            print(f"Запрос на {amount}")
            self.lock.acquire()
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
            finally:
                self.lock.release()

            time.sleep(0.001)  # Задержка


# Создание объекта Bank
bk = Bank()

# Создание потоков
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args = (bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f"Итоговый баланс: {bk.balance}")
