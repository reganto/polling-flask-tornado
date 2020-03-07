from urllib.request import urlopen

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line


class IndexHandler(RequestHandler):
    def get(self):
        self.render("foo.html")

    def post(self):
        data = ""
        with urlopen("http://127.0.0.1:5000/polling/api/v1.0/rndimg") as response:
            for line in response:
                data += line.decode("utf-8")

        self.write(data)


if __name__ == "__main__":
    parse_command_line()
    app = Application(
        handlers=[
            (r"/", IndexHandler),
        ],
        template_path="templates",
        static_path="static",
        debug=True,
    )
    app.listen(8000)
    instance = IOLoop.instance()
    instance.start()
