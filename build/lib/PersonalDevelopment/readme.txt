������ ������� �� �����
1) ��������� anaconda prompt
2) set VENV=c:\Projects\PersonalDevelopment
3) %VENV%\Scripts\pserve development.ini --reload

�������� ����� �������
1) � ����� models ������� ����� �������
2) � ����� models � __init__.py ������� ������ ������ �������
3) Migrate the database with Alembic
3.1) %VENV%\Scripts\alembic -c development.ini revision --autogenerate -m "use new models Page and User"
3.2) %VENV%\Scripts\alembic -c development.ini upgrade head
