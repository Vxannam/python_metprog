import os.path
import random


def generator_data(_len): # функция для генерации выборки определенного размера
    if not os.path.isfile(f'./gen_data/car_data_{_len}.txt'): # проверка создана ли уже выборка такого размера
        with open('./data/car_model.txt', mode='r', encoding='UTF-8') as car_model:
            with open('./data/date.txt', mode='r', encoding='UTF-8') as date:
                with open('./data/car_number.txt', mode='r') as car_number:
                    with open('./data/car_color.txt', mode='r', encoding='UTF-8') as car_color:
                        car_model = car_model.readlines()
                        dates = date.readlines()
                        car_number = car_number.readlines()
                        car_color = car_color.readlines()
                        with open('./data/surname_man.txt', mode='r', encoding='UTF-8') as surname_man:
                            with open('./data/name_man.txt', mode='r', encoding='UTF-8') as name_man:
                                with open('./data/patronymic_man.txt', mode='r', encoding='UTF-8') as patronymic_man:
                                    surnames_man = surname_man.readlines()
                                    names_man = name_man.readlines()
                                    patronymics_man = patronymic_man.readlines()
                                    with open('./data/surname_woman.txt', mode='r', encoding='UTF-8') as surname_woman:
                                        with open('./data/name_woman.txt', mode='r', encoding='UTF-8') as name_woman:
                                            with open('./data/patronymic_woman.txt', mode='r', encoding='UTF-8') as patronymic_woman:
                                                surnames_woman = surname_woman.readlines()
                                                names_woman = name_woman.readlines()
                                                patronymics_woman = patronymic_woman.readlines()
        with open(f'./gen_data/car_data_{_len}.txt', mode='w', encoding='UTF8') as car_data:
            for i in range(_len):
                if random.randint(0, 1): # 0 - женский пол, 1 - мужской пол
                    fio_title_date_pages = f"{surnames_man[random.randint(0, len(surnames_man) - 1)].strip()} {names_man[random.randint(0, len(names_man) - 1)].strip()} {patronymics_man[random.randint(0, len(patronymics_man) - 1)].strip()} | {car_model[random.randint(0, len(car_model) - 1)].strip()} | {dates[random.randint(0, len(dates) - 1)].strip()} | {car_number[random.randint(0, len(car_number) - 1)].strip()} | {car_color[random.randint(0, len(car_color) - 1)].strip()}"
                    if i == _len - 1:
                        car_data.write(fio_title_date_pages) # записываем выборку в файл
                    else:
                        car_data.write(fio_title_date_pages + '\n') # записываем выборку в файл
                else:
                    fio_title_date_pages = f"{surnames_woman[random.randint(0, len(surnames_woman) - 1)].strip()} {names_woman[random.randint(0, len(names_woman) - 1)].strip()} {patronymics_woman[random.randint(0, len(patronymics_woman) - 1)].strip()} | {car_model[random.randint(0, len(car_model) - 1)].strip()} | {dates[random.randint(0, len(dates) - 1)].strip()} | {car_number[random.randint(0, len(car_number) - 1)].strip()} | {car_color[random.randint(0, len(car_color) - 1)].strip()}"
                    if i == _len - 1:
                        car_data.write(fio_title_date_pages) # записываем выборку в файл
                    else:
                        car_data.write(fio_title_date_pages + '\n') # записываем выборку в файл
