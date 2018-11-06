from tornado.web import RequestHandler
import json

class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        greeting=self.get_argument('greeting','hello ')
        self.write(greeting+' tornado user')

class TextHandler(RequestHandler):

    def initialize(self,name,hobby):
        self.name = name
        self.hobby = hobby

    def get(self,*args,**kwargs):
        print(self.name,self.hobby)
        self.write('hello')

class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            'name':'bon',
            'age':21,
            'weight':70,
            'height':186
        }
        jsonStr = json.dumps(per)
        self.write(jsonStr)


class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            'name':'bon',
            'age':21,
            'weight':70,
            'height':186
        }

        self.write(per)
