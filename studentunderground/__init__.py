from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from studentunderground.security import groupfinder
from studentunderground.models.site import SiteModel
from studentunderground.handlers.test import TestHandler

def main(global_config, **settings):
    '''Main config function'''
 
    authn_policy = AuthTktAuthenticationPolicy('sosecret',
                                               callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy() 
    config = Configurator(settings=settings,
                          root_factory=SiteModel,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          default_permission='view')

    config.add_static_view(name='static', path='studentunderground:static')

    #Handlers
    config.include('pyramid_handlers')
    #Handler Root Routes
    config.add_handler('test_root', '/test', handler=TestHandler, action='index')

    #Handler Action Routes
    config.add_handler('test_action', '/test/{action}', handler=TestHandler)

    return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5432")
