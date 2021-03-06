from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields

from sync.models import Open

class urlencodeSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'urlencode']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'html': 'text/html',
        'plist': 'application/x-plist',
        'urlencode': 'application/x-www-form-urlencoded',
        }

class UserResource(ModelResource):
	class Meta:
		resource_name = 'user'
		queryset = User.objects.all()
		filtering = {
			"username": ALL,
		}
		allowed_methods = ['get','post','put','delete']
		serializer = urlencodeSerializer()
		authentication = Authentication()
		authorization = Authorization()

	def determine_format(self, request):
		return 'application/json'

class OpenResource(ModelResource):
	user = fields.ForeignKey(UserResource,'user')

	class Meta:
		queryset = Open.objects.all()
		resource_name = 'open'
		filtering = {
			"name": ALL,
			"user": ALL_WITH_RELATIONS,
		}
		allowed_methods = ['get','post','put','delete']
		serializer = urlencodeSerializer()
		authentication = Authentication()
		authorization = Authorization()
		
	def determine_format(self, request):
		return 'application/json'
		
