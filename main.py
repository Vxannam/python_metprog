import time

from classion import CarData, MultiMap
from generation import generator_data
from random_fio import random_fio
from search import linear_search, binary_search
from sortirovki import merge_sort

sizes = [100, 1000, 5000, 10000, 15000, 25000, 50000, 75000, 100000]

for size in sizes:
    generator_data(size)

fio = random_fio()

for size in sizes:
    data = []
    multimap = MultiMap()

    with open(f'./gen_data/car_data_{size}.txt', mode='r', encoding='UTF-8') as car_data:
        for line in car_data:  # читаем строчку из файла
            car_data = CarData(line.strip())  # получаем объект класса CarData
            data.append(car_data)  # добавляем в массив объект
            multimap.insert(car_data.fio, car_data)  # добавляем ключ и объект в multimap
        start = time.time()  # запускаем таймер
        res = linear_search(data, fio)  # линейный поиск в массиве
        end = time.time()  # останавливаем таймер

        print(f'size: {size} Линейный поиск в массиве: {str(end - start).replace(".", ",")}, len_res: {len(res)}, ' f' result = {res[0].fio if res else res}, key = {fio}')  # выводим результат

        start1 = time.time()
        data = merge_sort(data)  # сортируем слиянием
        start = time.time()  # запускаем таймер
        res = binary_search(data, fio)  # бинарный поиск в массиве
        end = time.time()  # останавливаем таймер
        end1 = time.time()

        print(f'size: {size} Бинарный поиск в массиве: {str(end - start).replace(".", ",")}, len_res: {len(res)}, ' f'result = {res[0].fio if res else res}, key = {fio}')  # выводим результат
        print(f'size: {size} Бинарный поиск в массиве + сортировка: {str(end1 - start1).replace(".", ",")}')
        start = time.time()  # запускаем таймер
        res = multimap.find(fio)  # поиск в multimap
        end = time.time()  # останавливаем таймер
        print(f'size: {size} Поиск в multimap: {str(end - start).replace(".", ",")}, len_res: {len(res)}, ' f'result = {res[0].val.fio if res else res}, key = {fio}') # выводим результат
        print()
