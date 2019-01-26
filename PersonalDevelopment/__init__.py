from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid.security import unauthenticated_userid

from PersonalDevelopment import models


def get_user(request):
    # the below line is just an example, use your own method of
    # accessing a database connection here (this could even be another
    # request property such as request.db, implemented using this same
    # pattern).
    userid = unauthenticated_userid(request)
    if userid is not None:
        # this should return None if the user doesn't exist
        # in the database
        return request.dbsession.query(models.User).filter(models.User.id == userid).one()


class AccessFactory(object):
    def __init__(self, request):
        self.__acl__ = [
            (Allow, Everyone, 'view'),
        ]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # with Configurator(settings=settings) as config:
    with Configurator(settings=settings, root_factory=AccessFactory) as config:
        authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
        authz_policy = ACLAuthorizationPolicy()

        config.set_authentication_policy(authn_policy)
        config.set_authorization_policy(authz_policy)
        config.add_request_method(get_user, 'user', reify=True)

        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
