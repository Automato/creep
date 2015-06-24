import tornado.ioloop
import tornado.web

class CardHandler(tornado.web.RequestHandler):
	
	def delete(self):
		self.write("Delete goes here")
	
	def get(self):
		self.set_status(204)
		self.set_header('Accept', 'GET, HEAD, OPTIONS, POST')
		raise tornado.web.Finish()
		
	def head(self):
		self.write("Head goes here")
		
	def options(self):
		self.write("Options goes here")
		
	def patch(self):
		self.write("Patch goes here")
		
	def post(self):
		self.write("Post goes here")
	
	def put(self):
		self.write("Put goes here")


def main():
	routes = [
		(r'/cards', CardHandler),
	]
	application = tornado.web.Application(routes)
	application.listen(80)
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()
