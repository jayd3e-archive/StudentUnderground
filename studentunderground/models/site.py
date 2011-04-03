from pyramid.security import Allow
from pyramid.security import Everyone

class SiteModel(object):
    '''Root object, more information to be inserted later'''
    
    __name__ = None
    __parent__ = None
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:admins', 'edit') ]

    def __init__(self, request):
        pass
