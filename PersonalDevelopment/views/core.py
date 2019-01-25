from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config
import re

from PersonalDevelopment import models


@view_config(route_name='main_page', renderer='../static/MainPage.jinja2')
def main_view(request):
    return {}


@view_config(route_name='user_main', renderer='../templates/user_main.jinja2')
def user_main(request):
    return {}
