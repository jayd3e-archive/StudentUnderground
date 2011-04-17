from pyramid_handlers import action

class FeedHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='feed/index.mako')
    def index(self):
        title = "S2S | Feed"
        return {'here':self.here,
                'title':title}
