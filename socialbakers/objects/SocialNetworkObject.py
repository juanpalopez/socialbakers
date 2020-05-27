import urllib
import json
import itertools

from socialbakers import urls
from socialbakers import apiconfig
from datetime import datetime
from datetime import timedelta
from time import sleep

class SocialNetworkObject(object):

	def __init__(self, socialnetwork = None):
		self.socialnetwork = socialnetwork
		self.base_url = urls.SocialBakersUrls.BASE_URL
		self.version = apiconfig.socialbakers_config['API_VERSION']
		self.url = '%s/%s/%s' % (self.base_url, self.version, self.socialnetwork)

	class Metric:
		pass

	def get_profiles(self):
		profiles_url = '%s/profiles' % (self.url,)
		response = urllib.request.urlopen(profiles_url)
		return response.read()

	def get_metrics(self,date_start, date_end, profiles, metrics):
		metrics_url = '%s/metrics' % (self.url,)

		headers = {}
		headers['Content-Type'] = 'application/json; charset=utf-8'

		parameters = {
				"date_start": date_start,
				"date_end": date_end,
				"profiles": profiles,
				"metrics": metrics
				}

		encoded_data = json.dumps(parameters)
		request = urllib.request.Request(metrics_url, data=encoded_data, headers=headers)

		response = urllib.request.urlopen(request)

		return json.loads(response.read())

	def get_metrics_split_fields(self,date_start, date_end, profiles, metrics):

		num_metrics = len(metrics) 

		if num_metrics < 26:
			return self.get_metrics(date_start, date_end, profiles, metrics)
		else:

			data1 = self.get_metrics(date_start, date_end, profiles, metrics[:25])
			data2 = self.get_metrics(date_start, date_end, profiles, metrics[25:])
			# print(data1)
			ids = [profile['id'] for  profile in data1['profiles'] ]
			sub_data1 = [profile['data'] for  profile in data1['profiles']]
			sub_data2 = [profile['data'] for  profile in data2['profiles']]

			zipped_sub_data = zip(sub_data1,sub_data2)


			metrics_data = []
			for profile in zipped_sub_data:
				expanded_data = []
				for metrics1, metrics2 in zip(profile[0], profile[1]):
					expanded_data.append(self.merge(metrics1, metrics2))
				


				metrics_data.append(expanded_data)


			sb_data = []
			for data, sb_id in zip(metrics_data, ids):
				sb_data.append({'data': data, 'id': sb_id})
				


			result = {'success':True}
			result['profiles'] = sb_data

			return result
				
	def get_metrics_split_profiles(self,date_start, date_end, profiles, metrics):

		floor = 0
		ceiling = 25
		profiles_data = []
		num_profiles = len(profiles)

		while ceiling < num_profiles:
			# print("%s:%s" % (floor,ceiling))
			
			data = self.get_metrics_split_fields(date_start, date_end, profiles[floor:ceiling], metrics)
			# print data
			self.list_merge(profiles_data, data['profiles'])
			# profiles_data.extend(data['profiles'][0]['data'])

			floor += 25
			ceiling += 25
			sleep(2)


		ceiling = num_profiles
		# print("%s:%s" % (floor, ceiling) )

		data = self.get_metrics_split_fields(date_start, date_end, profiles[floor:ceiling], metrics)
		self.list_merge(profiles_data, data['profiles'])

		result = {'success':True}
		result['profiles'] = profiles_data
		return result


	def merge(self, dict_a, dict_b):
		# list_a.extend(list_b)
		# return list_a
		dict_copy = dict_a.copy()
		dict_copy.update(dict_b)
		return dict_copy

	def list_merge(self, list_a, list_b):
		list_a.extend(list_b)
		return list_a

	def get_bulk_metrics(self,date_start, date_end, profiles, metrics):
		tr = self.time_range(date_start,date_end)
		profiles_data = []

		# print(tr)
		if tr <= 90:
			return self.get_metrics_split_profiles(date_start, date_end, profiles, metrics)

		else:
			while self.time_range(date_start,date_end) > 90:
				
				data = self.get_metrics_split_profiles(date_start, self.add_time(date_start,90), profiles, metrics)
				self.list_merge(profiles_data, data['profiles'])
				print('.',)
				# result.extend()
				# data = self.get_metrics(date_start, self.add_time(date_start,90), profiles, metrics)
				# result.extend(data['profiles'][0]['data'])

				date_start = self.add_time(date_start,91)
				print("looping")

			print(date_start)
			print(date_end)

			data = self.get_metrics_split_profiles(date_start, date_end, profiles, metrics)
			self.list_merge(profiles_data, data['profiles'])

		# return result
		result = {'success':True}
		result['profiles'] = profiles_data
		# print result_dict
		return result


	def time_range(self, date_start, date_end):
		pattern = '%Y-%m-%d'
		time_range = datetime.strptime(date_end, pattern) - datetime.strptime(date_start, pattern)
		return time_range.days

	def add_time(self,date_start, days):
		pattern = '%Y-%m-%d'
		new_date = datetime.strptime(date_start, pattern) + timedelta(days=days)
		return datetime.strftime(new_date, pattern)


def split_metrics_request(self,date_start, date_end, profiles, metrics):
	pass


class FacebookObject(SocialNetworkObject):
	def __init__(self):
		self._isFacebook = True
		super(FacebookObject, self).__init__('facebook')

	class Metric(SocialNetworkObject.Metric):
		comments_count = 'comments_count'
		comments_count_by_paid_status = 'comments_count_by_paid_status'
		comments_count_by_type = 'comments_count_by_type'
		fans_change = 'fans_change'
		fans_count_lifetime = 'fans_count_lifetime'
		fans_count_lifetime_by_country = 'fans_count_lifetime_by_country'
		interactions_count = 'interactions_count'
		interactions_count_by_paid_status = 'interactions_count_by_paid_status'
		interactions_count_by_type = 'interactions_count_by_type'
		interactions_per_1000_fans = 'interactions_per_1000_fans'
		interactions_per_1000_fans_by_type = 'interactions_per_1000_fans_by_type'
		page_posts_by_app = 'page_posts_by_app'
		page_posts_count = 'page_posts_count'
		page_posts_count_by_paid_status = 'page_posts_count_by_paid_status'
		page_posts_count_by_type = 'page_posts_count_by_type'
		reactions_count = 'reactions_count'
		reactions_count_by_paid_status = 'reactions_count_by_paid_status'
		reactions_count_by_reaction_type = 'reactions_count_by_reaction_type'
		reactions_count_by_type = 'reactions_count_by_type'
		shares_count = 'shares_count'
		shares_count_by_paid_status = 'shares_count_by_paid_status'
		shares_count_by_type = 'shares_count_by_type'
		user_posts_average_response_time = 'user_posts_average_response_time'
		user_posts_by_app = 'user_posts_by_app'
		user_posts_count = 'user_posts_count'
		user_posts_responded_by_time = 'user_posts_responded_by_time'
		user_posts_responded_count = 'user_posts_responded_count'
		user_posts_response_rate = 'user_posts_response_rate'
		user_questions_average_response_time = 'user_questions_average_response_time'
		user_questions_count = 'user_questions_count'
		user_questions_responded_by_time = 'user_questions_responded_by_time'
		user_questions_responded_count = 'user_questions_responded_count'
		user_questions_response_rate = 'user_questions_response_rate'

class TwitterObject(SocialNetworkObject):
	def __init__(self):
		self._isTwitter = True
		super(TwitterObject, self).__init__('twitter')

	class Metric(SocialNetworkObject.Metric):
		ff_ratio = 'ff_ratio'
		followers_change = 'followers_change'
		followers_count_lifetime = 'followers_count_lifetime'
		incoming_count = 'incoming_count'
		incoming_questions_average_response_time = 'incoming_questions_average_response_time'
		incoming_questions_count = 'incoming_questions_count'
		incoming_questions_responded_by_time = 'incoming_questions_responded_by_time'
		incoming_questions_responded_count = 'incoming_questions_responded_count'
		incoming_questions_response_rate = 'incoming_questions_response_rate'
		incoming_replies_count = 'incoming_replies_count'
		incoming_retweets_count = 'incoming_retweets_count'
		incoming_tweets_average_response_time = 'incoming_tweets_average_response_time'
		incoming_tweets_count = 'incoming_tweets_count'
		incoming_tweets_responded_by_time = 'incoming_tweets_responded_by_time'
		incoming_tweets_responded_count = 'incoming_tweets_responded_count'
		incoming_tweets_response_rate = 'incoming_tweets_response_rate'
		interactions_count = 'interactions_count'
		interactions_per_1000_followers = 'interactions_per_1000_followers'
		likes_count = 'likes_count'
		listed_change = 'listed_change'
		listed_count_lifetime = 'listed_count_lifetime'
		profile_activities_by_app = 'profile_activities_by_app'
		profile_activities_count = 'profile_activities_count'
		profile_replies_count = 'profile_replies_count'
		profile_retweets_count = 'profile_retweets_count'
		profile_tweets_count = 'profile_tweets_count'
		replies_count = 'replies_count'

class InstagramObject(SocialNetworkObject):
	def __init__(self):
		self._isInstagram = True
		super(InstagramObject,self).__init__('instagram')

	class Metric(SocialNetworkObject.Metric):
		comments_count = 'comments_count'
		comments_count_by_post_image_filter = 'comments_count_by_post_image_filter'
		comments_count_by_post_type = 'comments_count_by_post_type'
		comments_count_by_post_video_filter = 'comments_count_by_post_video_filter'
		followers_change = 'followers_change'
		followers_count_lifetime = 'followers_count_lifetime'
		following_change = 'following_change'
		following_count_lifetime = 'following_count_lifetime'
		interactions_count = 'interactions_count'
		interactions_count_by_post_image_filter = 'interactions_count_by_post_image_filter'
		interactions_count_by_post_type = 'interactions_count_by_post_type'
		interactions_count_by_post_video_filter = 'interactions_count_by_post_video_filter'
		interactions_per_1000_followers = 'interactions_per_1000_followers'
		interactions_per_1000_followers_by_image_filter = 'interactions_per_1000_followers_by_image_filter'
		interactions_per_1000_followers_by_type = 'interactions_per_1000_followers_by_type'
		interactions_per_1000_followers_by_video_filter = 'interactions_per_1000_followers_by_video_filter'
		likes_count = 'likes_count'
		likes_count_by_post_image_filter = 'likes_count_by_post_image_filter'
		likes_count_by_post_type = 'likes_count_by_post_type'
		likes_count_by_post_video_filter = 'likes_count_by_post_video_filter'
		posts_count = 'posts_count'
		posts_count_by_image_filter = 'posts_count_by_image_filter'
		posts_count_by_type = 'posts_count_by_type'
		posts_count_by_video_filter = 'posts_count_by_video_filter'

class YoutubeObject(SocialNetworkObject):
	def __init__(self):
		self._isYoutube = True
		super(YoutubeObject,self).__init__('youtube')

	class Metric(SocialNetworkObject.Metric):
		comments_change = 'comments_change'
		dislikes_change = 'dislikes_change'
		interaction_change = 'interaction_change'
		interactions_per_1000_subscribers = 'interactions_per_1000_subscribers'
		likes_change = 'likes_change'
		subscribers_change = 'subscribers_change'
		subscribers_count_lifetime = 'subscribers_count_lifetime'
		video_change = 'video_change'
		video_count_lifetime = 'video_count_lifetime'
		viewed_time_change = 'viewed_time_change'
		viewed_time_lifetime = 'viewed_time_lifetime'
		views_change = 'views_change'
		views_count_lifetime = 'views_count_lifetime'

class PinterestObject(SocialNetworkObject):
	def __init__(self):
		self._isPinterest = True
		super(PinterestObject,self).__init__('pinterest')

	class Metric(SocialNetworkObject.Metric):
		boards_change = 'boards_change'
		boards_count_lifetime = 'boards_count_lifetime'
		comments_count = 'comments_count'
		followers_change = 'followers_change'
		followers_count_lifetime = 'followers_count_lifetime'
		following_change = 'following_change'
		following_count_lifetime = 'following_count_lifetime'
		interactions_count = 'interactions_count'
		likes_count = 'likes_count'
		pins_change = 'pins_change'
		pins_count_lifetime = 'pins_count_lifetime'
		repin_count = 'repin_count'

class SocialNetworkCatalog(object):

	def __init__(self):
		self.profiles_lists = []

	def profile_list_splitter(self, profile_list):
		return [profile_list[x:x+25] for x in xrange(0, len(profile_list), 25)]

	def date_splitter(self, date_start, date_end):
		dates = []
		while SocialbakersUtils().time_range(date_start, date_end) > 90:
			dates.append((date_start, SocialbakersUtils().add_time(date_start,90)) )
			date_start = SocialbakersUtils().add_time(date_start,90)
		dates.append((date_start,date_end))
		return dates



class SocialbakersUtils(object):
	def time_range(cls, date_start, date_end):
		pattern = '%Y-%m-%d'
		time_range = datetime.strptime(date_end, pattern) - datetime.strptime(date_start, pattern)
		return time_range.days

	def add_time(cls,date_start, days):
		pattern = '%Y-%m-%d'
		new_date = datetime.strptime(date_start, pattern) + timedelta(days=days)
		return datetime.strftime(new_date, pattern)