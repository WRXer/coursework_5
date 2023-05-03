from src.auth_data import user, password

import psycopg2

def dump_db(hh_vacancies):
    # Установка соединения с БД
    conn = psycopg2.connect(host="localhost", database="hh_db", user=user, password=password)
    employers_data = []
    vacancies_data = []

    for v in hh_vacancies:
        if len(v) > 1:
            z = (v['vacancy']['name'], v['vacancy']['area'], v['vacancy']['url'], v['vacancy']['description'],
                 v['vacancy']['payment_from'], v['vacancy']['payment_to'], v['employer']['id'])
            vacancies_data.append(z)
            if v['employer']['address'] is not None:
                x = (v['employer']['id'], v['employer']['name'], v['employer']['address']['city'], v['employer']['emp_url'])
            else:
                x = (v['employer']['id'], v['employer']['name'], v['employer']['address'], v['employer']['emp_url'])
            employers_data.append(x)

    try:
        with conn:
            with conn.cursor() as cur:  # create cursor
                # Добавление данных о работодателях
                for employer in employers_data:
                    employer = [None if value is None else value for value in employer]    # заменяем значения None на NULL
                    cur.execute(
                        """
                        INSERT INTO employers (emp_id, name, emp_address, emp_url)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (name) DO UPDATE    
                        SET emp_address = EXCLUDED.emp_address
                        """,
                        employer
                    )

                # Добавление данных о вакансиях
                for vacancy in vacancies_data:
                    vacancy = [None if value is None else value for value in vacancy]    # заменяем значения None на NULL
                    cur.execute(
                        """
                        INSERT INTO vacancies (name, area, vac_url, description, salary_from, salary_to, employer_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (vac_url) DO UPDATE    
                        SET description = EXCLUDED.description
                        """,
                        vacancy
                    )
    finally:
        conn.close()  # close connection to db закрываем соединение