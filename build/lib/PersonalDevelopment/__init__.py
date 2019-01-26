from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow
from pyramid.security import Everyone


# class AccessFactory(object):
#     def __init__(self, request):
#         self.__acl__ = [
#             (Allow, Everyone, 'view'),
#             (Allow, 'Daniil1', 'radar')
#         ]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
    # with Configurator(settings=settings, root_factory=AccessFactory) as config:
        # authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
        # authz_policy = ACLAuthorizationPolicy()

        # config.set_authentication_policy(authn_policy)
        # config.set_authorization_policy(authz_policy)

        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
