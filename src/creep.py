import uuid
from json import JSONDecodeError
import tornado.ioloop
import tornado.web
import tornado.escape
from .api import APIHandler
from .boards import BoardHandler
from .cards import CardHandler
from .categories import CategoryHandler


ghetto_db = {
    'cards': {},
    'categories': {},
    'boards': {},
}

class CardHandler(tornado.web.RequestHandler):

    def delete(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                self.set_status(200)
                self.write(ghetto_db['cards'].pop(card_id))
            else:
                self.set_status(404)
                self.write({'error': 'card id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'DELETE not allowed without card id'})

        raise tornado.web.Finish()

    def get(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                self.set_status(200)
                self.write(ghetto_db['cards'][card_id])
            else:
                self.set_status(404)
                self.write({'error': 'card id not found'})
        else:
            self.set_status(200)
            self.write(ghetto_db)

        raise tornado.web.Finish()

    def head(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                self.set_status(200)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db['cards'][card_id]))
                )
            else:
                self.set_status(404)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode({'error': 'card id not found'}))
                )
        else:
            self.set_status(200)
            self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db))
            )

        raise tornado.web.Finish()

    def options(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                self.set_status(200)
                self.set_header('Accept', 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT')
            else:
                self.set_status(404)
                self.write({'error': 'card id not found'})

        else:
            self.set_status(200)
            self.set_header('Accept', 'GET, HEAD, OPTIONS, POST')

        raise tornado.web.Finish()

    def patch(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                self.set_status(200)
                self.write("Patch goes here")
            else:
                self.set_status(404)
                self.write({'error': 'card id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PATCH not allowed without card id'})

        raise tornado.web.Finish()

    def post(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                self.set_status(409)
                self.write({'error': 'card id already exists'})
            else:
                self.set_status(405)
                self.write({'error': 'POST not allowed with card id'})
        else:
            card_id = str(uuid.uuid4())
            while card_id in ghetto_db['cards']:
                card_id = str(uuid.uuid4())
            try:
                card = tornado.escape.json_decode(self.request.body)
            except JSONDecodeError:
                self.set_status(400)
                self.write({'error': 'Malformed JSON request'})
                raise tornado.web.Finish()
            self.set_status(201)
            ghetto_db['cards'][card_id] = card
            self.write({'id': card_id, 'content': card})

        raise tornado.web.Finish()

    def put(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db['cards']:
                try:
                    card = tornado.escape.json_decode(self.request.body)
                except JSONDecodeError:
                    self.set_status(400)
                    self.write({'error': 'Malformed JSON request'})
                    raise tornado.web.Finish()
                self.set_status(200)
                ghetto_db['cards'][card_id] = card
                self.write({'id': card_id, 'content': card})
            else:
                self.set_status(404)
                self.write({'error': 'card id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PUT not allowed without card id'})

        raise tornado.web.Finish()


class CategoryHandler(tornado.web.RequestHandler):

    def delete(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.write(ghetto_db['categories'].pop(card_id))
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'DELETE not allowed without category id'})

        raise tornado.web.Finish()

    def get(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.write(ghetto_db['categories'][card_id])
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(200)
            self.write(ghetto_db['categories'])

        raise tornado.web.Finish()

    def head(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db['cateogies'][category_id]))
                )
            else:
                self.set_status(404)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode({'error': 'category id not found'}))
                )
        else:
            self.set_status(200)
            self.set_header('Content-Length',
                len(tornado.escape.json_encode(ghetto_db['cards']))
            )

        raise tornado.web.Finish()

    def options(self, category_id=None):
        global ghetto_db

        if category_id:
            if cateogry_id in ghetto_db['categories']:
                self.set_status(200)
                self.set_header('Accept', 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT')
            else:
                self.set_Status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(200)
            self.set_header('Accept', 'GET, HEAD, OPTIONS, POST')

        raise tornado.web.Finish()

    def patch(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.write("Patch goes here")
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PATCH not allowed without card id'})

        raise tornado.web.Finish()

    def post(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(409)
                self.write({'error': 'category id already exists'})
            else:
                self.set_status(405)
                self.write({'error': 'POST not allowed with category id'})
        else:
            category_id = str(uuid.uuid4())
            while category_id in ghetto_db['categories']:
                category_id = str(uuid.uuid4())
            try:
                category = tornado.escape.json_decode(self.request.body)
            except JSONDecodeError:
                self.set_status(400)
                self.write({'error': 'Malformed JSON request'})
                raise tornado.web.Finish()
            self.set_status(201)
            ghetto_db['categories'][category_id] = category
            self.write({'id': category_id, 'content': category})

        raise tornado.web.Finish()

    def put(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                category = tornado.escape.json_decode(self.request.body)
                ghetto_db['categories'][category_id] = category
                self.write({'id': category_id, 'content': category})
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PUT not allowed without category id'})

        raise tornado.web.Finish()


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

