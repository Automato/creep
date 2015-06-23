import tornado.ioloop
import tornado.web

class CardHandler(tornado.web.RequestHandler):
	
	def get(self):
		self.write("Hello World!")


def main():
	routes = [
		(r'/cards', CardHandler),
	]
	application = tornado.web.Application(routes)
	application.listen(80)
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()
