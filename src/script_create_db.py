"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

def create_db():
    #connect to db подключение к бд
    conn = psycopg2.connect(host="localhost", database="hh_db", user="postgres", password="777Nokia13")

    try:
        with conn:
            with conn.cursor() as cur:    #create cursor
                cur.execute(
                    """
                    CREATE TABLE employers (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        description TEXT,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        phone VARCHAR(20),
                        emp_url VARCHAR(255)
                    )
                    """
                )    # Создание таблицы работодателей

                cur.execute(
                    """
                    CREATE TABLE vacancies (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        description TEXT,
                        salary NUMERIC(10, 2),
                        employer_id INTEGER REFERENCES employers(id) ON DELETE CASCADE,
                        area VARCHAR(50) NOT NULL,
                        vac_url VARCHAR(255)
                        )
                    """
                )     # Создание таблицы вакансий


    finally:
        conn.close()    #close connection to db закрываем соединение
