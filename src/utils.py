from src.engine_classes import HH


















def main():
    s_q = 'Точка'
    hh = HH(s_q)  # hh = HH(search_query) ИНИТИ Точка Softline Predicto Skyeng Технопром Автомакон Idaproject МВП Цифровые решения
    hh_vacancies = hh.get_request()
    print(hh_vacancies)
