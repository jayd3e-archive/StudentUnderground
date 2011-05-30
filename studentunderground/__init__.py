from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.exceptions import Forbidden
from studentunderground.handlers.site import SiteHandler
from studentunderground.handlers.article import ArticleHandler
from studentunderground.handlers.group import GroupHandler
from studentunderground.handlers.hw import HwHandler
from studentunderground.handlers.setting import SettingHandler
from studentunderground.handlers.user import UserHandler
from studentunderground.handlers.exceptions import notFound
from studentunderground.handlers.exceptions import forbidden
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
    config.add_handler('article_root', '/articles', handler=ArticleHandler, action='index')
    config.add_handler('group_root', '/groups', handler=GroupHandler, action='index')
    config.add_handler('hw_root', '/hw', handler=HwHandler, action='index')
    config.add_handler('setting_root', '/settings', handler=SettingHandler, action='index')
    config.add_handler('user_root', '/user', handler=UserHandler, action='index')

    #Handler Action Routes
    config.add_handler('site_action', '/{action}', handler=SiteHandler)
    config.add_handler('article_action', '/articles/{action}', handler=ArticleHandler)
    config.add_handler('group_action', '/groups/{action}', handler=GroupHandler)
    config.add_handler('hw_action', '/hw/{action}', handler=HwHandler)
    config.add_handler('setting_action', '/settings/{action}', handler=SettingHandler)
    config.add_handler('user_action', '/user/{action}', handler=UserHandler)
    
    #Exception Views
    config.add_view(notFound,
                    context=NotFound,
                    permission='__no_permission_required__',
                    renderer='exceptions/not_found.mako')
    config.add_view(forbidden,
                    context=Forbidden,
                    permission='__no_permission_required__')

    return config.make_wsgi_app()

if __name__ == '__main__':
    from paste.httpserver import serve
    serve(main(), host="0.0.0.0", port="5432")
