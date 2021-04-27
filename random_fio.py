import random

def random_fio():
    with open('./data/surname_man.txt', mode='r', encoding='UTF-8') as surname_man:
        with open('./data/name_man.txt', mode='r', encoding='UTF-8') as name_man:
            with open('./data/patronymic_man.txt', mode='r', encoding='UTF8') as patronymic_man:
                surnames_man = surname_man.readlines()
                names_man = name_man.readlines()
                patronymics_man = patronymic_man.readlines()
                with open('./data/surname_woman.txt', mode='r', encoding='UTF-8') as surname_woman:
                    with open('./data/name_woman.txt', mode='r', encoding='UTF-8') as name_woman:
                        with open('./data/patronymic_woman.txt', mode='r',  encoding='UTF-8') as patronymic_woman:
                            surnames_woman = surname_woman.readlines()
                            names_woman = name_woman.readlines()
                            patronymics_woman = patronymic_woman.readlines()
    if random.randint(0, 1): # 0 - женский пол, 1 - мужской пол
        fio = f"{surnames_man[random.randint(0,len(surnames_man) - 1)].strip()} {names_man[random.randint(0,len(names_man) - 1)].strip()} {patronymics_man[random.randint(0, len(patronymics_man) - 1)].strip()}"
    else:
        fio = f"{surnames_woman[random.randint(0,len(surnames_woman) - 1)].strip()} {names_woman[random.randint(0,len(names_woman) - 1)].strip()} {patronymics_woman[random.randint(0, len(patronymics_woman) - 1)].strip()}"
    return fio
