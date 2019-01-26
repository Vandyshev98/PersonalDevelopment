from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.security import remember
from pyramid.security import forget
import re

from PersonalDevelopment import models


@view_config(route_name='registration', renderer='../templates/registration.jinja2')
def registration(request):
    if (request.POST is not None) & (len(request.POST) > 0):
        # пробуем зарегестрироваться
        try:
            # получаем входные данные
            user_email = request.params.get('email')
            user_name = request.params.get('name')
            user_password = request.params.get('password')
            user_password_repeat = request.params.get('passwordRepeat')

            # сообщим пользователю если что то пошло не так
            message = correct_registration_input_data(user_email, user_password, user_password_repeat)
            if not message:
                return {'message': message}

            # создаем объект пользователя и записываем его в БД
            new_user = models.User(login=user_email, name=user_name)
            new_user.set_password(user_password)
            request.dbsession.add(new_user)
            return HTTPFound(location='user_main')
        except Exception as ex:
            print(ex)
            return {'message': 'Ошибка на стороне сервера'}
    if request.user:
        return HTTPFound(location='user_main')
    return {}


@view_config(route_name='login', renderer='../templates/login.jinja2')
def login(request):
    if (request.POST is not None) & (len(request.POST) > 0):
        # пробуем войти
        try:
            # получаем входные данные
            user_email = request.params.get('email')
            user_password = request.params.get('password')
            remeber_user = request.params.get('remember')

            # если поля пустые то они пустые строки
            if correct_login_input_data(user_email, user_password):
                user_in_list = request.dbsession.query(models.User).filter(models.User.login == user_email).all()
                if not user_in_list:
                    return {'message': 'Нет пользователя с таким логином'}
                user = user_in_list.pop(0)
                if user.check_password(user_password):
                    # запоминаем пользователя
                    headers = remember(request, user.id)
                    return HTTPFound(location='user_main', headers=headers)
                else:
                    return {'message': 'Неверный пароль'}
            else:
                return {'message': 'Некоректный логин/пароль'}
        except Exception as ex:
            print(ex)
            return {'message': 'Ошибка на стороне сервера'}
    if request.user:
        return HTTPFound(location='user_main')
    return {}


@view_config(route_name='logout', renderer='../templates/login.jinja2')
def logout(request):
    # забываем пользователя
    headers = forget(request)
    return HTTPFound(location='login', headers=headers)


def correct_registration_input_data(email, password, password_repeat):
    """
    проверка на корректность логина и пароля пользователя при регистрации
    :param email: пользователя
    :param password: пароль
    :param password_repeat: повторенный пароль
    :return:
    """
    if re.match(r'[A-Za-z0-9@#$%,.^&+=]{8,}', password) is None:
        return 'Некоректный пароль'
    if re.match(r'[A-Za-z0-9@#$%,.^&+=]{8,}', password_repeat) is None:
        return 'Некоректный пароль'
    if re.match(r'[A-Za-z0-9@#$%,.^&+=]{5,}', email) is None:
        return 'Некоректный email'
    if password != password_repeat:
        return 'Пароли не совпадают'
    return ""


def correct_login_input_data(email, password):
    """
    проверка на корректность логина и пароля пользователя при входе
    :param email: пользователя
    :param password: пользователя
    :return:
    """
    # пароль не меньше 8 символов
    if re.match(r'[A-Za-z0-9@#$%,.^&+=]{8,}', password):
        if re.match(r'[A-Za-z0-9@#$%,.^&+=]{5,}', email):
            return True
    return False
