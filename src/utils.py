from src.engine_classes import HH
from src.script_create_db import create_db
from src.script_dump import dump_db
from src.unique_params import create_params

import psycopg2


def main():
    try:
        create_db()
        create_params()
    except psycopg2.errors.DuplicateTable:
        print('ОШИБКА:  отношение "employers" уже существует')

    hh_vacancies = []
    emp_q = ['ИНИТИ', 'Точка', 'Softline', 'Predicto', 'Skyeng', 'Технопром', 'Автомакон', 'ГоИНВЕСТ', 'МВП', 'ПРОМФИНСТРОЙ']
    for s in emp_q:
        hh = HH(s)  # hh = HH(search_query) ИНИТИ Точка Softline Predicto Skyeng Технопром Автомакон ГоИНВЕСТ МВП ПРОМФИНСТРОЙ
        hh_vac = hh.get_request()
        hh_vacancies = hh_vacancies + hh_vac
    dump_db(hh_vacancies)

