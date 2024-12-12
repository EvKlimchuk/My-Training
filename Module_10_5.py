import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == "__main__":
    # Подготовка файлов для чтения
    filenames = [f'./file {i}.txt' for i in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейное выполнение: {linear_duration:.4f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.time() - start_time
    print(f"Многопроцессное выполнение: {parallel_duration:.4f} секунд")
