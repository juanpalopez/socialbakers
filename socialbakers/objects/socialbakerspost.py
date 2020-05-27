import urllib
import json

from socialbakers import urls
from socialbakers import apiconfig

class SocialbakersPostObject(object):

	def __init__(self, socialnetwork = None):
		self.socialnetwork = socialnetwork
		self.base_url = urls.SocialBakersUrls.BASE_URL
		self.version = apiconfig.socialbakers_config['API_VERSION']
		self.url = '%s/%s/%s' % (self.base_url, self.version, self.socialnetwork)

	def get_fields(self, date_start, date_end, profile, fields):
		'''Base object for each individual post for a given profile
		'''
		fields_url = '%s/page/posts' % (self.url,)

		headers = {}
		headers['Content-Type'] = 'application/json; charset=utf-8'

		parameters = {
				"date_start": date_start,
				"date_end": date_end,
				"profile": profile,
				"fields": fields
				}

		encoded_data = json.dumps(parameters)
		print(encoded_data)
		request = urllib.request.Request(fields_url, data=encoded_data, headers=headers)

		response = urllib.request.urlopen(request)

		return response.read()

	class Field(object):
		pass
			

class FacebookPost(SocialbakersPostObject):
	'''Each individual post in a Facebook profile
    '''

	def __init__(self):
		self._isFacebookPost = True
		super(FacebookPost,self).__init__('facebook')

	class Field(SocialbakersPostObject.Field):
		attachments = 'attachments'
		author_id = 'author_id'
		comments_count = 'comments_count'
		created = 'created'
		post_id = 'id'
		interactions_count = 'interactions_count'
		message = 'message'
		page_id = 'page_id'
		reactions = 'reactions'
		reactions_count = 'reactions_count'
		shares_count = 'shares_count'
		story = 'story'
		status_type = 'type'
		url = 'url'
		