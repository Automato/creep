import tornado.ioloop
import tornado.web
from .api import APIHandler
from .boards import BoardHandler
from .cards import CardHandler
from .categories import CategoryHandler


ghetto_db = {
    'cards': {},
    'categories': {},
    'boards': {},
}


def main():
    routes = [
        (r'/', APIHandler),
        (r'/cards', CardHandler),
        (r'/cards/(?P<card_id>[^\/]+)', CardHandler),
        (r'/categories', CategoryHandler),
        (r'/categories/(?P<category_id>[^\/]+)', CategoryHandler),
        (r'/boards', BoardHandler),
        (r'/boards/(?P<board_id>[^\/]+)', BoardHandler),
    ]
    application = tornado.web.Application(routes)
    application.listen(80)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

