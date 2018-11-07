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
#预先设置
class HeaderHandler(RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type",'text/html;charset=UTF-8')


    def get(self, *args, **kwargs):
        pass

class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            'name':'bon',
            'age':21,
            'weight':70,
            'height':186
        }
        # 将字典转换成字符串
        jsonStr = json.dumps(per)
        self.set_header("Content-Type",'application/json; charset=UTF-8')
        self.set_header('uname','bon')
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
