import uuid
from json import JSONDecodeError
import tornado.ioloop
import tornado.web
import tornado.escape

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
