from pyramid_handlers import action
from studentunderground.handlers.handler import Handler

class TestHandler(Handler):
    @action(renderer='layouts/test.mako')
    def style(self):
        return {}
