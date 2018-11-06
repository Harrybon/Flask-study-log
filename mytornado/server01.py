import config
from tornado.ioloop import IOLoop
from application import Application
from tornado.httpserver import HTTPServer


if __name__ == "__main__":

    app = Application()
    # http_server = HTTPServer(app)
    # http_server.bind(options.port)
    # http_server.start(num)
    # http_server.listen(config.options['port'])
    app.listen(config.options['port'])
    IOLoop.instance().start()