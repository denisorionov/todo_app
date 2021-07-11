# Список задач
http://todo58.herokuapp.com/

Приложение реализовано на Python 3.8.

Использованы фреймворки:
Django 3.2;
Django Rest Framework 3.12.

## Реализованы следующие функции:
* Создание, удаление, редактирование задачи.
* Наличие статуса выполнения и срока выполнения задачи.
* Сортировка задач по категориям/тегам/статусу выполнения.
* Возможность отслеживания истории изменения задач.
* Поиск по задачам.
* Импорт и экспорт задач в .csv.

## API:
api/

Доступные методы: GET, POST, PUT

Примеры запросов:


```shell script
GET /api/

Ответ:
HTTP 200 OK
Allow: GET, POST, PUT, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 2,
        "title": "Go to gym",
        "description": "workout",
        "due_date": "2021-07-11",
        "status": "done"
    }
]

или

curl -X GET http://todo58.herokuapp.com/api/

Ответ:
[{
    "id":1,
    "title":"Create ToDo app",
    "description":"test",
    "due_date":"2021-07-11",
    "status":"in progress"
  },
  {
    "id":2,
    "title":"Go to gym",
    "description":"workout",
    "due_date":"2021-07-11",
    "status":"done"
  }]
```
```shell script
curl -X POST -d "{\"title\":\"Create\",\"description\":\"test\",\"due_date\":\"2021-07-11\",\"status\":\"done\"}" 
-H "Content-Type: application/json" http://todo58.herokuapp.com/api/

Ответ:

  {
    "title":"Create",
    "description":"test",
    "due_date":"2021-07-11",
    "status":"done"
  }
```
api_detail/{int:id}/

Примеры запросов:

```shell script
GET /api_detail/1/

Ответ:
HTTP 200 OK
Allow: GET, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "title": "Create ToDo app",
    "description": "test",
    "due_date": "2021-07-11",
    "status": "in progress"
}
```

```shell script
DELETE /api_detail/1/?format=api

Ответ:
HTTP 204 No Content
Allow: GET, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```


## Установка проекта.
1. [Установить Python.](https://www.python.org/downloads/)
2. Скачать проект.
3. Создать виртуальное окружение: python -m venv env
4. Активировать виртуальное окружение: source env/scripts/activate
5. Установить зависимости: pip install -r requirements.txt
7. Выполнить миграции ./manage.py migrate
8. Запустить проект: ./manage.py runserver
9. Открыть в браузере: http://localhost:8000.

Для тестирования:
логин: admin;
пароль: admin

## Предложения по дальнейшему развитию реализованного приложения.
* Добавить возможность регистарции пользователей.
* Добавить уведомления о истечении срока исполнения задачи.
