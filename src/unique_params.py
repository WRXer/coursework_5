import psycopg2
from src.auth_data import user, password


def create_params():
    #connect to db подключение к бд
    conn = psycopg2.connect(host="localhost", database="hh_db", user=user, password=password)
    try:
        with conn:
            with conn.cursor() as cur:    #create cursor
                cur.execute(
                    """
                    CREATE UNIQUE INDEX idx_emp_name ON employers (name);
                    """
                )     #Защита от дублей в таблице

                cur.execute(
                    """
                    CREATE UNIQUE INDEX idx_vacancies_url ON vacancies (vac_url);
                    """
                )    #Защита от дублей в таблице
    finally:
        conn.close()    #close connection to db закрываем соединение
