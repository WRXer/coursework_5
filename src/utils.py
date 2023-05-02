from src.engine_classes import HH








def main():
    hh_vacancies = []
    s_q = ['ИНИТИ', 'Точка', 'Softline', 'Predicto', 'Skyeng', 'Технопром', 'Автомакон', 'ГоИНВЕСТ', 'МВП', 'ПРОМФИНСТРОЙ']
    for s in s_q:
        hh = HH(s)  # hh = HH(search_query) ИНИТИ Точка Softline Predicto Skyeng Технопром Автомакон ГоИНВЕСТ МВП ПРОМФИНСТРОЙ
        hh_vac = hh.get_request()
        hh_vacancies = hh_vacancies + hh_vac
    for v in hh_vacancies:
        if len(v) > 1:
            print(v)
