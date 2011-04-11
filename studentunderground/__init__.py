from pyramid.config import Configurator
from studentunderground.models.site import SiteModel

def main(global_config, **settings):
    '''Main config function'''
 
    config = Configurator(settings=settings,
                          root_factory=SiteModel)

    config.add_static_view(name='static', path='studentunderground:static')

    #Handlers
    config.include('pyramid_handlers')
    #Handler Root Routes

    #Handler Action Routes

    return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5432")
