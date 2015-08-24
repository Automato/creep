import uuid
from json import JSONDecodeError
import tornado.ioloop
import tornado.web
import tornado.escape
import .db.model


class Card(db.model):
    
    def __init__(self):
        pass
    
    def create(self):
        pass
    
    def delete(self):
        pass
    
    def update(self):
        pass
    
    def read(self):
        pass

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
