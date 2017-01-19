import unittest
import socialbakers.api

from unittest import TestCase


class TestApi(TestCase):
	global token, secret
	token = 'MjMzNzcyXzM5MzM0NV8xNzkyNDA4OTE5MjQ3XzUzYzUwNjU2YzQyN2MyOGUyOTY2MTdiNGU1YTc0Zjhh'
	secret = '5aa58b075ebb8e92d5d8b72da1b1ccac'

	def test_socialbakersapi(self):
		print type(socialbakers.api.SocialBakersApi.init(token,secret))

if __name__ == '__main__':
	unittest.main()
