
Socialbakers Api Wrapper
=======================

This proyect is intended to ease the access to Socialbakers API.


Installation
------------

Socialbakers is supported on python 2.7. The recommended way to install is via `pip`

.. code-block:: bash

   pip install socialbakers


Quickstart
----------

To use start using `socialbakers`API you will need to have a TOKEN and SECRET

.. code-block:: bash
	
	from socialbakers import api
	from socialbakers.objects import socialnetworkobject

	token = '<YOUR-TOKEN>'
	secret= '<YOUR-SECRET>'

	#Initialize API
	api.SocialbakersApi.init(token, secret)

	#There is an object for each Social Network(Facebook, Twitter, Instagram, Youtube, Pinterest)
	fb = FacebookObject()

	Check Fields Available in ./socialbakers/objects/socialnetworkobject
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

	#Get profiles added to your account
	profiles = fb.get_profiles()

	#Get Metrics from each profile
	result = fb.get_metrics('2017-01-01', '2017-01-20',['12345','23456','34567'], fb_fields)








