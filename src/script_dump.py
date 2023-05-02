import psycopg2

# Установка соединения с БД
conn = psycopg2.connect(host="localhost", database="hh_db", user="postgres", password="777Nokia13")

try:
    with conn:
        with conn.cursor() as cur:  # create cursor
            # Добавление данных о работодателях
            employers_data = []

            for employer in employers_data:
                cur.execute(
                    """
                    INSERT INTO employers (name, emp_url)
                    VALUES (%s, %s)
                    """,
                    employer
                )

            # Добавление данных о вакансиях
            vacancies_data = []

            for vacancy in vacancies_data:
                cur.execute(
                    """
                    INSERT INTO vacancies (name, description, salary, employer_id, area, vac_url)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    vacancy
                )
finally:
    conn.close()  # close connection to db закрываем соединение