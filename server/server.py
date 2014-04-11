import flashreview
import cherrypy
from cherrypy.lib.static import serve_file
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))
class HelloWorld:
	def __init__(self):
		pass

	@cherrypy.expose
	def index(self):
		return serve_file(os.path.join(current_dir,"index.html"))

	api = flashreview.FlashReview()

config={
	'/static': {
		"tools.staticdir.root": current_dir,
		"tools.staticdir.on": True,
		"tools.staticdir.dir": "static"
	}
}

cherrypy.config.update({'server.socket_host': '0.0.0.0',
						'server.socket_port': 80,
					   })

cherrypy.quickstart(HelloWorld(), config = config)

