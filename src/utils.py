from src.engine_classes import HH
from src.script_create_db import create_db
import psycopg2






def main():
    try:
        create_db()
    except psycopg2.errors.DuplicateTable:
        print('ОШИБКА:  отношение "employers" уже существует')

    hh_vacancies = []
    emp_q = ['ИНИТИ', 'Точка', 'Softline', 'Predicto', 'Skyeng', 'Технопром', 'Автомакон', 'ГоИНВЕСТ', 'МВП', 'ПРОМФИНСТРОЙ']
    for s in emp_q:
        hh = HH(s)  # hh = HH(search_query) ИНИТИ Точка Softline Predicto Skyeng Технопром Автомакон ГоИНВЕСТ МВП ПРОМФИНСТРОЙ
        hh_vac = hh.get_request()
        hh_vacancies = hh_vacancies + hh_vac
    for v in hh_vacancies:
        if len(v) > 1:

            print(v['employer']['name'], v['employer']['emp_url'])
