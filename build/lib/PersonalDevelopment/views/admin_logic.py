from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
import sqlalchemy as sa

from PersonalDevelopment import models


@view_config(route_name='check_db', renderer='../templates/test.jinja2')
def check_db(request):
    user_list = request.dbsession.query(models.User).all()
    for user in user_list:
        print(user)
    return {}
