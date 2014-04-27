from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from sync import views

urlpatterns = patterns("",
		url(r'^$',views.start,name="start"),
    	url(r'^accounts/login/$',views.login,name="login"),
    	url(r'^accounts/logout/$', views.logout,name="logout"),
    	url(r'^accounts/register/$',views.register,name="register"),
    	url(r'^accounts/profile/$',views.profile,name="profile"),
    	url(r'^accounts/groups/$',views.groups,name="groups"),
    	url(r'^accounts/groups/new$',views.new_group,name="new_group"),
    	url(r'^accounts/groups/add$',views.add_to_group,name="add_to_group"),
    	url(r'^accounts/groups/accept/(?P<inv_id>\d+)$',views.accept_invitation,name="accept_invitation"),
		)
		
