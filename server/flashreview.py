import json
import cherrypy
import pymongo

class FlashReview:
	exposed = True

	def __init__(self):
		self.db = pymongo.Connection().FlashReview

	@cherrypy.expose
	def submitreview(self, **kwargs):
		self.db.reviews.insert(kwargs)
		raise cherrypy.HTTPRedirect('/')

	@cherrypy.expose
	def getreviews(self):
		reviews = []

		for review in self.db.reviews.find().sort('_id', pymongo.DESCENDING):
			del review['_id']
			reviews.append(review)

		return json.dumps(reviews)