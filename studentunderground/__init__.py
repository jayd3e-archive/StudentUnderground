from pyramid.config import Configurator
from studentunderground.handlers.feed import SiteHandler
from studentunderground.models.site import SiteModel
from studentunderground.db.config import DbConfig
from studentunderground.models.base import initializeDb
from studentunderground.models.base import engine

def main(global_config, **settings):
    '''Main config function'''
    initializeDb(engine(DbConfig))

    config = Configurator(settings=settings,
                          root_factory=SiteModel)

    config.add_static_view(name='static', path='studentunderground:static')

    #Includes
    config.include('pyramid_handlers')
    config.include('pyramid_tm')
    #Handler Root Routes
    config.add_handler('site_root', '/', handler=SiteHandler, action='index')
    #Handler Action Routes
    config.add_handler('site_action', '/{action}', handler=SiteHandler)

    return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5432")
