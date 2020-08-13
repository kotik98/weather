# Умный сервис прогноза погоды
## Средний уровень сложности
- Проектирование сервиса: <br />
    Сервис спроектирован с использованием Flask — фреймворка для создания веб-приложений на языке программирования Python.
    Это простое веб приложение, которое вставляет полученные с API данные в шаблон и предоставляет их пользователю.
- Процесс работы программы: <br />
    + Пользователь вводит в форму название города
    + Сервер пытается узнать погоду для выбраного города
    + Формируется страничка ответа
- Запуск программы
    + В виртуальном окружении установить фреймворки из requirements.txt
    + Зарегистрироваться на openweathermap.org, получить свой API key, сохранить его в текстовом файле в директории проекта под именем app_id.txt
    + Запустите файл weather.py с помощью вашего интерпретатора Python
    + Проследовав по ссылке http://127.0.0.1:5000/ вы увидите интерфейс приложения
