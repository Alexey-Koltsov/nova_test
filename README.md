# nova_test
Тестовое задание от NOVA: сделать API метод, который создает в google drive документ

#Описание проекта «NOVA_TEST»

Проект NOVA_TEST делает POST запрос с параметрами: 
1. data = Текстовое содержимое файла
2. name = Название файла
и создает в публичной папке Novatest в Google Drive документ с названием = name и содержимым = data:
https://drive.google.com/drive/folders/1nX-d27PxbC3Zefbtqs8vavWI-k4lAZSu?usp=drive_link
Для этого создан пустой Google account и авторизовано приложение в Google Drive, получены токены.

#Стек использованных технологий

- Python3
- Django Framework
- Django Rest Framework
- Postman
- SQLite3

#Как запустить проект

##Клонировать репозиторий и перейти в него в командной строке
```
git clone git@github.com:Alexey-Koltsov/nova_test.git
```
```
cd nova_test
```
##Cоздать виртуальное окружение

Windows
```
python -m venv venv
```
##Активировать виртуальное окружение Windows
```
source venv/Scripts/activate
```
LinuxmacOS
```
python3 -m venv venv source venvbinactivate
```
##Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
LinuxmacOS
```
python3 -m pip install --upgrade pip
```
##Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
##Выполнить миграции

Windows
```
python manage.py makemigrations
```
```
python manage.py migrate
```
LinuxmacOS
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
##Запустить проект

Windows
```
python manage.py runserver
```
LinuxmacOS
```
python3 manage.py runserver
```


#Создание в Google Drive документа

Создать в Google Drive документ с названием = name и содержимым = data

POST http://127.0.0.1:8000/api/v1/filecreate/

```
{
  "data": "Hello World!",
  "name": "Hello.txt"
}
```
Пример ответа:
```
{
  "data": "Hello World!",
  "name": "Hello.txt"
}
``

#Автор: Кольцов Алексей.
