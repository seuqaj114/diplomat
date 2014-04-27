from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from tastypie.api import Api
from sync.api import OpenResource, UserResource

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(OpenResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^',include("sync.urls", namespace="home")),
	url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
