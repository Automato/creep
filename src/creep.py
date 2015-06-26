import uuid
import tornado.ioloop
import tornado.web
import tornado.escape

ghetto_db = {}

class CardHandler(tornado.web.RequestHandler):
	
	def delete(self):
		self.write("Delete goes here")
	
	def get(self, card_id=None):
		if card_id:
			global ghetto_db

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
			

	def head(self):
		self.write("Head goes here")
		
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
		
	def patch(self):
		self.write("Patch goes here")
		
	def post(self, card_id=None):
		global ghetto_db

		if card_id:
			if card_id in ghetto_db:
				self.set_status(409)
				self.write({'error': 'card id already exists'})
			else:
				self.set_status(405)
				self.write({'error': 'POST not allowed with cardId'})
		else:
			self.set_status(201)
			card_id = str(uuid.uuid4())
			while card_id in ghetto_db:
				card_id = str(uuid.uuid4())
			card = tornado.escape.json_decode(self.request.body)
			self.write({'id': card_id, 'content': card})

		raise tornado.web.Finish()
	
	def put(self):
		self.write("Put goes here")


def main():
	routes = [
		(r'/cards', CardHandler),
		(r'/cards/(?P<card_id>[^\/]+)', CardHandler)
	]
	application = tornado.web.Application(routes)
	application.listen(80)
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()
