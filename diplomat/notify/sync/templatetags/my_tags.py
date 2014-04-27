from django import template
from django.contrib.auth.models import User, Group
from sync.models import *

register = template.Library()

@register.simple_tag
def get_group_from_id(group_id):
	try:
		return Group.objects.get(pk=group_id).name
	except Group.DoesNotExist:
		return "Unknown"

@register.simple_tag
def get_user_from_id(user_id):
	try:
		return User.objects.get(pk=user_id).username
	except User.DoesNotExist:
		return "Unknown"
		



