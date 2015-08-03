import uuid
from json import JSONDecodeError
import tornado.ioloop
import tornado.web
import tornado.escape


ghetto_db = {
    'cards': {},
    'categories': {},
    'boards': {},
}


class APIHandler(tornado.web.RequestHandler):

    def delete(self):
        self.set_status(405)
        self.write({'error': 'DELETE not allowed on API root'})

    def get(self):
        self.set_status(200)
        self.write({
            'cardURL': '/cards{/cardId}',
            'categoryURL': '/categories{/categoryId}',
            'boardURL': '/boards{/boardId}',
        })

    def head(self):
        self.set_status(200)
        self.set_header('Content-Length',
            len(tornado.escape.json_encode({
                'cardURL': '/cards{/cardId}',
                'categoryURL': '/categories{/categoryId}',
                'boardURL': '/boards{/boardId}',
            }))
        )
        raise self.tornado.web.Finish()

    def options(self):
        self.set_status(200)
        self.set_headers('Accept', 'GET, HEAD, OPTIONS')

    def patch(self):
        self.set_status(403)
        self.write({'error': 'PATCH not allowed on API root'})

    def post(self):
        self.set_status(405)
        self.write({'error': 'POST not allowed on API root'})

    def put(self):
        self.set_status(405)
        self.write({'error': 'PUT not allowed on API root'})


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

class BoardHandler(tornado.web.RequestHandler):

    def delete(self, board_id=None):
        global ghetto_db

        if board_id:
            if board_id in ghetto_db['boards']:
                self.set_status(200)
                self.write(ghetto_db['boards'].pop(card_id))
            else:
                self.set_status(404)
                self.write({'error': 'board id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'DELETE not allowed without board id'})

        raise tornado.web.Finish()

    def get(self, board_id=None):
        global ghetto_db

        if board_id:
            if board_id in ghetto_db['boards']:
                self.set_status(200)
                self.write(ghetto_db['boards'][card_id])
            else:
                self.set_status(404)
                self.write({'error': 'board id not found'})
        else:
            self.set_status(200)
            self.write(ghetto_db['boards'])

        raise tornado.web.Finish()

    def head(self, board_id=None):
        global ghetto_db

        if board_id:
            if board_id in ghetto_db['boards']:
                self.set_status(200)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db['cateogies'][board_id]))
                )
            else:
                self.set_status(404)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode({'error': 'board id not found'}))
                )
        else:
            self.set_status(200)
            self.set_header('Content-Length',
                len(tornado.escape.json_encode(ghetto_db['cards']))
            )

        raise tornado.web.Finish()

    def options(self, board_id=None):
        global ghetto_db

        if board_id:
            if cateogry_id in ghetto_db['boards']:
                self.set_status(200)
                self.set_header('Accept', 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT')
            else:
                self.set_Status(404)
                self.write({'error': 'board id not found'})
        else:
            self.set_status(200)
            self.set_header('Accept', 'GET, HEAD, OPTIONS, POST')

        raise tornado.web.Finish()

    def patch(self, board_id=None):
        global ghetto_db

        if board_id:
            if board_id in ghetto_db['boards']:
                self.set_status(200)
                self.write("Patch goes here")
            else:
                self.set_status(404)
                self.write({'error': 'board id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PATCH not allowed without card id'})

        raise tornado.web.Finish()

    def post(self, board_id=None):
        global ghetto_db

        if board_id:
            if board_id in ghetto_db['boards']:
                self.set_status(409)
                self.write({'error': 'board id already exists'})
            else:
                self.set_status(405)
                self.write({'error': 'POST not allowed with board id'})
        else:
            board_id= str(uuid.uuid4())
            while board_id in ghetto_db['boards']:
                board_id= str(uuid.uuid4())
            try:
                board = tornado.escape.json_decode(self.request.body)
            except JSONDecodeError:
                self.set_status(400)
                self.write({'error': 'Malformed JSON request'})
                raise tornado.web.Finish()
            self.set_status(201)
            ghetto_db['boards'][board_id] = board
            self.write({'id': board_id, 'content': board})

        raise tornado.web.Finish()

    def put(self, board_id=None):
        global ghetto_db

        if board_id:
            if board_id in ghetto_db['boards']:
                self.set_status(200)
                board = tornado.escape.json_decode(self.request.body)
                ghetto_db['boards'][board_id] = board
                self.write({'id': board_id, 'content': board})
            else:
                self.set_status(404)
                self.write({'error': 'board id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PUT not allowed without board id'})

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

