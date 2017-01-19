import urllib2
import urllib
import json
import base64

class PreemptiveBasicAuthHandler(urllib2.HTTPBasicAuthHandler):
    '''Preemptive basic auth.

    Instead of waiting for a 403 to then retry with the credentials,
    send the credentials if the url is handled by the password manager.
    Note: please use realm=None when calling add_password.'''
    def http_request(self, req):
        url = req.get_full_url()
        realm = None
        # this is very similar to the code from retry_http_basic_auth()
        # but returns a request object.
        user, pw = self.passwd.find_user_password(realm, url)
        if pw:
            raw = "%s:%s" % (user, pw)
            auth = 'Basic %s' % base64.b64encode(raw).strip()
            req.add_unredirected_header(self.auth_header, auth)
        return req

    https_request = http_request


class SocialBakersApi(object):

    BASE_URL = 'https://api.socialbakers.com/'
    '''
        Manage Basic Authentication with PreemptiveBasicAuthHandler
        and installing a global opener for following calls
    '''
    @classmethod
    def init(cls, token, secret):
        api_url = BASE_URL
        auth_handler = PreemptiveBasicAuthHandler()
        auth_handler.add_password(
            realm = None, # default realm.
            uri = api_url,
            user = token,
            passwd = secret)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
