#!/usr/local/bin/python3
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.websocket
import os
import requests
import json
from urllib.parse import urlparse
from twitter import *

#Base class for handlers
class BaseHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_header("Content-Type", "application/json")

#Index page
class mainHandler(BaseHandler):
	def get(self):
		self.render("index.html")
		
settings = {
	"static_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
	"debug": "True",
	"compress_response": "True"
}

def make_app():
	return tornado.web.Application([
		(r"/",mainHandler),
	], **settings)

if __name__ == "__main__":
	app = make_app()
	http_server = tornado.httpserver.HTTPServer(app)
	port = int(os.environ.get("PORT",5001))
	http_server.listen(port)
	print("Running at localhost: %d" % port)
	tornado.ioloop.IOLoop.current().start()
