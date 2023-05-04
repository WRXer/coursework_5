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
        self.data = []
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"text": self._search_query, "per_page": self._per_page}

    def get_request(self) -> list:
        response = requests.get(self.url, self.params)    # Отправка запроса к API
        if response.status_code == 200:    # Обработка ответа от API
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                if vacancy['employer']['name'] == self._search_query:
                    employer_id = vacancy['employer']['id']     # ID работодателя, для которого нужно получить список вакансий
                    employer_one = {'id': vacancy['employer']['id'], 'name': vacancy['employer']['name'],
                                                 'address': vacancy['address'], 'emp_url': vacancy['employer']['url']}
        else:
            print("Error:", response.status_code)

        url = f'https://api.hh.ru/vacancies?employer_id={employer_id}'    # URL запроса к API
        response = requests.get(url, self.params)    # Отправка запроса к API
        if response.status_code == 200:    # Обработка ответа от API
            vacancies = response.json()['items']    # Извлечение списка вакансий из ответа
            vacancies_for_employer = []    #Список вакансий по одному айди-работодателя
            for vacancy in vacancies:
                if vacancy['salary'] is not None:
                    vac_data = {'name': vacancy['name'], 'area': vacancy['area']['name'], 'url': vacancy['url'], 'description': vacancy['snippet']['requirement'],
                                                'payment_from': vacancy['salary']['from'],'payment_to': vacancy['salary']['to']}
                    vacancies_for_employer.append(vac_data)
                else:
                    continue
        else:
            print(f'Ошибка запроса: {response.status_code}')
        self.data.append({
            'employer': employer_one,
            'vacancies': vacancies_for_employer
        })
        return self.data