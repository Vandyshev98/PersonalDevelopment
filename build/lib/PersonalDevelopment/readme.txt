Запуск проекта по шагам
1) Запустить anaconda prompt
2) set VENV=c:\Projects\PersonalDevelopment
3) %VENV%\Scripts\pserve development.ini --reload

Создание новой таблицы
1) В папке models создать класс таблицы
2) В папке models в __init__.py сделать импорт класса таблицы
3) Migrate the database with Alembic
3.1) %VENV%\Scripts\alembic -c development.ini revision --autogenerate -m "use new models Page and User"
3.2) %VENV%\Scripts\alembic -c development.ini upgrade head
