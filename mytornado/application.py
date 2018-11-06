import tornado.web
import config
from views import index

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/test',index.TextHandler,{'name':'bon','hobby':'love'},),
            (r'/json01',index.JsonHandler),
            (r'/json02', index.Json2Handler)
        ]
        super(Application,self).__init__(handlers,**config.settings)

