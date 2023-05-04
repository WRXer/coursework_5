coursework_5 
Работа с базами данных 
Программа по сбору данных о компаниях с платформы HEAD HUNTER и их последующей обработкой через БД



-- Установка --
- Загрузить репозиторий
- Установить зависимости (pip install -r requirements.txt)
- Прописать данные для подключения к БД (создать файл auth_data(user=***, password=***))

--Описание--

Программа выполняет  запросы к платформе hh.ru

По умолчанию, список компаний: 'ИНИТИ', 'Точка', 'Softline', 'Predicto', 'Skyeng', 'Технопром', 'Автомакон', 'ГоИНВЕСТ', 'МВП', 'ПРОМФИНСТРОЙ'

Пользователь сам может указать компанию для получения данных

Пользователь сам может создать новую БД, либо выбрать старую

Данные сохраняются в БД, выбранную пользователем!

