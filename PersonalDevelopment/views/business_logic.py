from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError

from .. import models


@view_config(route_name='radar_example', renderer='../templates/radar_example.jinja2')
def radar_example(request):
    datasets = """[{"label":"2-я неделя","data":[8,15,10,8,4,2],"fill":true,"backgroundColor":"rgba(255, 99, 132, 0.2)","borderColor":"rgba(255,99,132,1)","borderWidth":2},{"label":"1-я неделя","data":[6,12,10,9,6,5],"fill":true,"backgroundColor":"rgba(54, 162, 235, 0.2)","borderColor":"rgba(54, 162, 235, 1)","borderWidth":2}]"""
    from pyramid.security import authenticated_userid
    user_id = authenticated_userid(request)
    return {"datasets": datasets, "user_id": user_id}


@view_config(route_name='statistics', renderer='../templates/statistics.jinja2')
def statistics(request):
    datasets = """[{"label":"2-я неделя","data":[8,15,10,8,4,2],"fill":true,"backgroundColor":"rgba(255, 99, 132, 0.2)","borderColor":"rgba(255,99,132,1)","borderWidth":2},{"label":"1-я неделя","data":[6,12,10,9,6,5],"fill":true,"backgroundColor":"rgba(54, 162, 235, 0.2)","borderColor":"rgba(54, 162, 235, 1)","borderWidth":2}]"""
    labels = """["Сон", "Работа", "Семья", "Друзья", "Хобби", "Учеба"]"""
    return {'datasets': datasets, 'labels': labels}


@view_config(route_name='create_directions', renderer='../templates/create_directions.jinja2')
def add_directions(request):
    return {}


@view_config(route_name='add_data', renderer='../templates/add_data.jinja2')
def add_data(request):
    return {}


