"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from src.auth_data import user, password
import csv

def create_db():
    #connect to db подключение к бд
    conn = psycopg2.connect(host="localhost", database="hh_db", user=user, password=password)

    try:
        with conn:
            with conn.cursor() as cur:    #create cursor
                cur.execute(
                    """
                    CREATE TABLE employers (
                        id SERIAL PRIMARY KEY,
                        emp_id integer,
                        name VARCHAR(255) NOT NULL,
                        emp_address VARCHAR(50),
                        emp_url VARCHAR(255)
                    )
                    """
                )    # Создание таблицы работодателей

                cur.execute(
                    """
                    CREATE TABLE vacancies (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        area VARCHAR(50) NOT NULL,
                        vac_url VARCHAR(255),
                        description TEXT,
                        salary_from INTEGER,
                        salary_to INTEGER,
                        employer_id INTEGER NOT NULL
                    )
                    """
                )     # Создание таблицы вакансий


    finally:
        conn.close()    #close connection to db закрываем соединение
