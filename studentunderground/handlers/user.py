from pyramid_handlers import action

class UserHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='user/index.mako')
    def index(self):
        title = "S2S | User"
        legend = "User"
        return {'here':self.here,
                'title':title}
