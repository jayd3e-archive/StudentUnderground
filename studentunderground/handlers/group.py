from pyramid_handlers import action

class GroupHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='group/index.mako')
    def index(self):
        title = "S2S | Groups"
        legend = "Groups"
        return {'here':self.here,
                'title':title,
                'legend':legend}