import uuid
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
        self.write({'error': 'PUT not allowed om API root'})
        

class CardHandler(tornado.web.RequestHandler):
    
    def delete(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db:
                self.set_status(200)
                self.write(ghetto_db.pop(card_id))
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
            if card_id in ghetto_db:
                self.set_status(200)
                self.write(ghetto_db[card_id])
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
            if card_id in ghetto_db:
                self.set_status(200)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db[card_id])))
            else:
                self.set_status(404)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode({'error': 'card id not found'})))
        else:
            self.set_status(200)
            self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db)))

        raise tornado.web.Finish()
        
    def options(self, card_id=None):
        if card_id:
            global ghetto_db

            if card_id in ghetto_db:
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
            if card_id in ghetto_db:
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
            if card_id in ghetto_db:
                self.set_status(409)
                self.write({'error': 'card id already exists'})
            else:
                self.set_status(405)
                self.write({'error': 'POST not allowed with card id'})
        else:
            self.set_status(201)
            card_id = str(uuid.uuid4())
            while card_id in ghetto_db:
                card_id = str(uuid.uuid4())
            card = tornado.escape.json_decode(self.request.body)
            ghetto_db[card_id] = card
            self.write({'id': card_id, 'content': card})

        raise tornado.web.Finish()
    
    def put(self, card_id=None):
        global ghetto_db

        if card_id:
            if card_id in ghetto_db:
                self.set_status(204)
                card = tornado.escape.json_decode(self.request.body)
                ghetto_db[card_id] = card
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
        self.write({'error': 'PUT not allowed om API root'})
        

class BoardHandler(tornado.web.RequestHandler):

    def delete(self):
        self.set_status(405)
        self.write({'error': 'DELETE not allowed on boards root'})


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

