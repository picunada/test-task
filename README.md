Test task №1 and №2

Для запуска приложения нужен docker и python 3.9.7

Запускалось на UNIX системе

Порядок запуска:
```
# Создаём и активируем окружение
python3 -m venv venv

source /venv/bin/activate

# Качаем зависисмости
python3 -m pip install -r requirements.txt

# Запускаем докер контейнер с бд
docker-compose -f docker-compose.yaml up 

# Запускаем приложение
uvicorn main:app --reload
# или
python3 main.py
```

Методы можно посмотреть и протестировать по ссылке http://127.0.0.1:8000/docs#/
