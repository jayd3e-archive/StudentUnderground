import unittest
from pyramid import testing
from studentunderground.models.base import initializeDb
from studentunderground.models.base import engine
from studentunderground.handlers.site import SiteHandler
from studentunderground.handlers.article import ArticleHandler
from studentunderground.handlers.group import GroupHandler
from studentunderground.handlers.hw import HwHandler
from studentunderground.handlers.setting import SettingHandler
from studentunderground.handlers.user import UserHandler
from studentunderground.db.config import TestConfig

class TestHandler(unittest.TestCase):
    def setUp(self):
        initializeDb(engine(TestConfig))
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.str_POST = {}
        self.request.environ['PATH_INFO'] = '/route'
                
        self.config.add_static_view(name='static', path='studentunderground:static')

        #Includes
        self.config.include('pyramid_handlers')
        self.config.include('pyramid_tm')
        
        #Handler Root Routes
        self.config.add_handler('site_root', '/', handler=SiteHandler, action='index')
        self.config.add_handler('article_root', '/articles', handler=ArticleHandler, action='index')
        self.config.add_handler('group_root', '/groups', handler=GroupHandler, action='index')
        self.config.add_handler('hw_root', '/hw', handler=HwHandler, action='index')
        self.config.add_handler('setting_root', '/settings', handler=SettingHandler, action='index')
        self.config.add_handler('user_root', '/user', handler=UserHandler, action='index')
    
        #Handler Action Routes
        self.config.add_handler('site_action', '/{action}', handler=SiteHandler)
        self.config.add_handler('article_action', '/articles/{action}', handler=ArticleHandler)
        self.config.add_handler('group_action', '/groups/{action}', handler=GroupHandler)
        self.config.add_handler('hw_action', '/hw/{action}', handler=HwHandler)
        self.config.add_handler('setting_action', '/settings/{action}', handler=SettingHandler)
        self.config.add_handler('user_action', '/user/{action}', handler=UserHandler)
        
    def tearDown(self):
        testing.tearDown()
                
class TestArticleHandler(TestHandler):
    def testArticleHandlerInit(self):
        handler = ArticleHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/route')

    def testArticleHandlerIndex(self):
        handler = ArticleHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('legend', response)
        
class TestGroupHandler(TestHandler):
    def testGroupHandlerInit(self):
        handler = GroupHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/route')

    def testGroupHandlerIndex(self):
        handler = GroupHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('legend', response)
        
class TestHwHandler(TestHandler):
    def testHwHandlerInit(self):
        handler = HwHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/route')

    def testHwHandlerIndex(self):
        handler = HwHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('legend', response)
        
class TestSettingHandler(TestHandler):
    def testSettingHandlerInit(self):
        handler = SettingHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/route')

    def testSettingHandlerIndex(self):
        handler = SettingHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('legend', response)
        
class TestSiteHandler(TestHandler):
    def testSiteHandlerInit(self):
        handler = SiteHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/route')

    def testSiteHandlerIndex(self):
        handler = SiteHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('legend', response)
        
class TestUserHandler(TestHandler):
    def testUserHandlerInit(self):
        handler = UserHandler(self.request)
        self.assertIsNot(handler.request, None)
        self.assertEqual(handler.here, '/route')

    def testUserHandlerIndex(self):
        handler = UserHandler(self.request)
        response = handler.index()
        self.assertIn('here', response)
        self.assertIn('title', response)
        self.assertIn('legend', response)