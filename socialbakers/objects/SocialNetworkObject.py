import urllib2
import json

from socialbakers import urls
from socialbakers import apiconfig

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
		response = urllib2.urlopen(profiles_url)
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
		request = urllib2.Request(metrics_url, data=encoded_data, headers=headers)

		response = urllib2.urlopen(request)

		return response.read()

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