from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    def __init__(self, search_query: str) -> None:
        self._search_query = search_query
        self._per_page = 100


    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    def __init__(self, search_query: str):
        super().__init__(search_query)
        self.vacancies_data = []
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"text": self._search_query, "per_page": self._per_page}

    def get_request(self) -> list:
        """
        Функция парсинга данных с ХХ
        :return:
        """
        response = requests.get(self.url, self.params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                if vacancy['employer']['name'] == self._search_query:
                    #print(vacancy)
                    if vacancy['salary'] is not None:
                        vacancy_data = {'employer': vacancy['employer']['name'], 'name': vacancy['name'], 'area': vacancy['area']['name'], 'url': vacancy['url'],
                                        'description': vacancy['snippet']['requirement'], 'payment': vacancy['salary']}
                        self.vacancies_data.append(vacancy_data)
                    else:
                        continue
        else:
            print("Error:", response.status_code)
        return self.vacancies_data
        #vacancy['salary'] зарплата
        #vacancy['snippet'] описание