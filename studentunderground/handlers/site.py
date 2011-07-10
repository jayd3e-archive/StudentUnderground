from pyramid_handlers import action

class SiteHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='site/index.mako')
    def index(self):
        title = "S2S | Feed"
        legend = "Site"
        return {'here':self.here,
                'title':title}
