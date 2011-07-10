from pyramid_handlers import action

class ArticleHandler(object):

    def __init__(self, request):
        self.request = request
        self.here = request.environ['PATH_INFO']

    @action(renderer='article/index.mako')
    def index(self):
        title = "S2S | Articles"
        legend = "Articles"
        return {'here':self.here,
                'title':title}