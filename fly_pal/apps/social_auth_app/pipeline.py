from django.http import HttpResponseRedirect
from social_auth.backends.facebook import FacebookBackend
from users.models import User
from social_auth.backends.twitter import TwitterBackend


#def user_details(backend, user, response, *args, **kwargs):
def user_details(backend, details, response, uid, user, social, *args, **kwargs):
	if backend.name == 'facebook':
		user.profile_img_url = response.get('picture')\
								.get('data')\
								.get('url')
		user.gender = response.get('gender')
		user.location = response.get('location').get('name')
		user.facebook_id = response.get('id')

	if backend.name == 'twitter':
		user.profile_img_url = response.get('profile_image_url')
		user.twitter_id = response.get('access_token')\
							.get('user_id')
		user.location = response.get('location')

	if user:
		if not user.has_usable_password():
			user.set_password("1234")
		user.save()
