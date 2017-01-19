import urllib
import urllib2
import base64
import unittest
import json

class SocialBakers(object):

	def __init__(self, token, secret):
		self.token = token
		self.secret = secret
		self.version = '0'

	def base_uri(self):
		return 'https://api.socialbakers.com/%s' % self.version 

	def base64_string(self):
		string64 = base64.b64encode('%s:%s' % (self.token, self.secret))
		return string64

	def basic_request(self, uri=None, params=None):
		if uri:
			url = self.base_uri() + uri
		else:
			url = self.base_uri()

		#Setting headers
		all_headers = {}
		all_headers['Authorization'] = 'Basic %s' % self.base64_string()
		all_headers['Content-Type'] = 'application/json; charset=utf-8'

		request = urllib2.Request(url, headers=all_headers)

		#POST if request has data else GET
		if params:
			encoded_data = json.dumps(params)
			request = urllib2.Request(url, data=encoded_data, headers=all_headers)

		response = urllib2.urlopen(request)

		return response


	'''
		Endpoints Methods
	'''
	def facebook_profiles(self):
		fb_profiles = json.loads(self.basic_request('/facebook/profiles').read())
		return fb_profiles

	def facebook_metrics(self, params=None):
		metrics = json.loads(self.basic_request('/facebook/metrics',params).read())
		return metrics


class TestSocialBakers(unittest.TestCase):
	global api, parameters
	token = 'MjMzNzcyXzM5MzM0NV8xNzkyNDA4OTE5MjQ3XzUzYzUwNjU2YzQyN2MyOGUyOTY2MTdiNGU1YTc0Zjhh'
	secret = '5aa58b075ebb8e92d5d8b72da1b1ccac'
	api = SocialBakers(token, secret)
	parameters = {
				  "date_start": "2016-01-01",
				  "date_end": "2016-01-30",
				  "profiles": ["131955860195741", "127448454020726"],
				  "metrics": ["fans_count_lifetime", "fans_change"]}	

	def test_base_uri(self):
		self.assertEqual(api.base_uri(),'https://api.socialbakers.com/0')

	
	def test_base64_string(self):
		self.assertEqual(api.base64_string(),'TWpNek56Y3lYek01TXpNME5WOHhOemt5TkRBNE9URTVNalEzWHpVell6VXdOalUyWXpReU4yTXlPR1V5T1RZMk1UZGlOR1UxWVRjMFpqaGg6NWFhNThiMDc1ZWJiOGU5MmQ1ZDhiNzJkYTFiMWNjYWM=')

	def test_basic_request_response_get_code_200(self):
		self.assertEqual(api.basic_request(uri='/facebook/profiles ').code,200)

	def test_facebook_profiles_success(self):
		self.assertEqual(api.facebook_profiles()['success'],True)

	def test_facebook_metrics_success(self):
		self.assertEqual(api.facebook_metrics(parameters)['success'],True)




if __name__ == '__main__':
	# unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSocialBakers)
	unittest.TextTestRunner(verbosity=2).run(suite)

	token = 'MjMzNzcyXzM5MzM0NV8xNzkyNDA4OTE5MjQ3XzUzYzUwNjU2YzQyN2MyOGUyOTY2MTdiNGU1YTc0Zjhh'
	secret = '5aa58b075ebb8e92d5d8b72da1b1ccac'
	api = SocialBakers(token, secret)
	parameters = {
					"date_start": "2016-01-01",
					"date_end": "2016-01-30",
					"profiles": ["318233611569188"],
					"metrics": ["comments_count"]
				}
	# print api.facebook_metrics(params=parameters)
	# print api.basic_request('/facebook/metrics',parameters).read()
	print api.facebook_profiles()


