from pyramid_handlers import action

class SettingHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='setting/index.mako')
    def index(self):
        title = "S2S | Settings"
        legend = "Settings"
        return {'here':self.here,
                'title':title}