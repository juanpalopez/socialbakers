import unittest
from socialbakers.api import SocialbakersApi
from socialbakers.objects.socialnetworkobject import (
	SocialNetworkObject,
	FacebookObject,
	TwitterObject,
	)

from unittest import TestCase


class SocialnetworkObject(unittest.TestCase):
	global token, secret, fb_fields, ids
	token = 'MjMzNzcyXzM5MzM0NV8xNzkyNDA4OTE5MjQ3XzUzYzUwNjU2YzQyN2MyOGUyOTY2MTdiNGU1YTc0Zjhh'
	secret = '5aa58b075ebb8e92d5d8b72da1b1ccac'
	SocialbakersApi.init(token,secret)
	fb_fields = [
		FacebookObject.Metric.comments_count_by_paid_status,
		FacebookObject.Metric.comments_count_by_type,
		FacebookObject.Metric.fans_change,
		FacebookObject.Metric.fans_count_lifetime,
		FacebookObject.Metric.fans_count_lifetime_by_country,
		FacebookObject.Metric.interactions_count,
		FacebookObject.Metric.interactions_count_by_paid_status,
		FacebookObject.Metric.interactions_count_by_type,
		FacebookObject.Metric.interactions_per_1000_fans,
		FacebookObject.Metric.interactions_per_1000_fans_by_type,
		FacebookObject.Metric.page_posts_by_app,
		FacebookObject.Metric.page_posts_count,
		FacebookObject.Metric.page_posts_count_by_paid_status,
		FacebookObject.Metric.page_posts_count_by_type,
		FacebookObject.Metric.reactions_count,
		FacebookObject.Metric.reactions_count_by_paid_status,
		FacebookObject.Metric.reactions_count_by_reaction_type,
		FacebookObject.Metric.reactions_count_by_type,
		FacebookObject.Metric.shares_count,
		FacebookObject.Metric.shares_count_by_paid_status,
		FacebookObject.Metric.shares_count_by_type,
		FacebookObject.Metric.user_posts_average_response_time,
		FacebookObject.Metric.user_posts_by_app,
		FacebookObject.Metric.user_posts_count,
		FacebookObject.Metric.user_posts_responded_by_time,
		FacebookObject.Metric.user_posts_responded_count,
		FacebookObject.Metric.user_posts_response_rate,
		FacebookObject.Metric.user_questions_average_response_time,
		FacebookObject.Metric.user_questions_count,
		FacebookObject.Metric.user_questions_responded_by_time,
		FacebookObject.Metric.user_questions_responded_count,
		FacebookObject.Metric.user_questions_response_rate,
	]
	ids = ['216143308403569',]

	def test_socialnetworkobject_time_range(self):
		fb = FacebookObject()
		self.assertEqual(1,fb.time_range('2017-01-01','2017-01-02'))
	
	def test_socialnetworkobject_add_time(self):
		fb = FacebookObject()
		self.assertEqual('2017-01-03',fb.add_time('2017-01-02',1))

	def test_socialnetworkobject_get_bulk_metrics_more90(self):
		fb = FacebookObject()
		self.assertTrue(fb.get_bulk_metrics('2016-01-01','2016-06-30', ids, fb_fields)['success'])

if __name__ == '__main__':
	unittest.main()
