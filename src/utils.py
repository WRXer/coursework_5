from src.engine_classes import HH
from src.sql.script_create_db import create_db
from src.sql.script_dump import dump_db
from src.sql.unique_params import create_params

import psycopg2


def start_choice():
    """
    Стартовая функция
    :return:
    """
    print("Для создания новой БД введите цифру '1'\nЕсли хотите работать со старой БД введите цифру '2'")
    return 2
    while True:
        choice_db = input()
        if choice_db == '1':
            print('Вы выбрали создание новой БД')
            return 1
        elif choice_db == '2':
            print('Вы выбрали старую БД')
            return 2
        else:
            print("Неверное значение! Введите цифру от 1-2!")

def db_choice():
    """
    Функция по выбору Базы Данных
    :return:
    """
    return 'teremok'
    s_c = start_choice()
    if s_c == 1:
        while True:
            try:
                database_name = input("Введите название новой БД или 'stop' для продолжения со старой БД\n")
                if database_name.lower() == 'stop':
                    database_name = input("Введите название старой БД\n")
                    break
                else:
                    create_db(database_name)
                    create_params(database_name)
                    print(f"Новая БД {database_name} создана")
                    break
            except psycopg2.errors.DuplicateTable:
                print('ОШИБКА:  отношение уже существует!')
    if s_c == 2:
        database_name = input("Введите название старой БД\n")
    return database_name

def employers_choice():
    """
    Функция ввода названия компании, по которой будет совершаться поиск вакансий
    :return:
    """
    hh_data = []
    while True:
        print("Если хотите найти вакансии: \nпо-новому работодателю: Нажмите '1'\nпо работодателям, установленным по умолчанию + новому: Нажмите '2'\nпо работодателям, установленным по умолчанию: Нажмите '3'\nдля выхода из данного меню: Нажмите '4'")
        user = input()
        #user = '1'
        if user == '1':
            while True:
                try:
                    emp_name = input("Введите название работодателя")
                    hh = HH(emp_name)  # hh = HH(search_query)
                    hh_vac = hh.get_request()
                    hh_data = hh_data + hh_vac
                    print("Парсинг выполнен")
                    break
                except UnboundLocalError:
                    print("Работодатель не найден")
        elif user == '2':
            emp_name = ['ИНИТИ', 'Точка', 'Softline', 'Predicto', 'Skyeng', 'Технопром', 'Автомакон', 'ГоИНВЕСТ', 'МВП', 'ПРОМФИНСТРОЙ']
            user_emp = input("Введите название работодателя")
            emp_name.append(user_emp)
            for s in emp_name:
                hh = HH(s)  # hh = HH(search_query)
                hh_vac = hh.get_request()
                hh_data = hh_data + hh_vac
            print("Парсинг выполнен")
            break
        elif user == '3':
            emp_name = ['ИНИТИ', 'Точка', 'Softline', 'Predicto', 'Skyeng', 'Технопром', 'Автомакон', 'ГоИНВЕСТ', 'МВП', 'ПРОМФИНСТРОЙ']
            for s in emp_name:
                hh = HH(s)  # hh = HH(search_query)
                hh_vac = hh.get_request()
                hh_data = hh_data + hh_vac
            print("Парсинг выполнен")
            break
        elif user == '4':
            break
        else:
            print("Неверное значение! Введите цифру от 1 - 4!")
    return hh_data


def main():
    print('Вас приветствует программа по работе с базой данных по плафторме hh.ru')
    database_name = db_choice()    #Выбор БД
    hh_data = employers_choice()    #Поиск по названию компании
    if hh_data is not None:
        dump_db(hh_data, database_name)    #Заливка данных в таблы



