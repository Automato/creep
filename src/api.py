import tornado.ioloop
import tornado.web
import tornado.escape

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

