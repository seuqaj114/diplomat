from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group
from django.contrib import auth
from sync.models import Open
from django.utils import timezone


class LoginForm(forms.Form):
	username = forms.CharField(max_length=50,)
	password = forms.CharField(max_length=50,widget=forms.PasswordInput())

	def clean(self):
		username=self.cleaned_data["username"]
		password=self.cleaned_data["password"]
		user=auth.authenticate(username=username,password=password)
		if user is None:
			raise forms.ValidationError("Sorry, the username or password were incorrect.")
		
		return self.cleaned_data
		
class RegisterForm(forms.Form):
	username = forms.CharField(max_length=50,)
	password = forms.CharField(max_length=50,widget=forms.PasswordInput())
	def clean(self):
		username=self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
			raise forms.ValidationError("Sorry, that username is already taken")
		except User.DoesNotExist:
			pass
			
		return self.cleaned_data
		
class NewGroupForm(forms.Form):
	def __init__(self,user,*args,**kwargs):
		self.user=user
		super(forms.Form,self).__init__(*args,**kwargs)

	name = forms.CharField(max_length=50,)
	
	#fazer clean para caracteres esquisitos
	def clean(self):
		name=self.cleaned_data["name"]
		try:
			self.user.groups.get(name=name)
			raise forms.ValidationError("Sorry, you already have a group with that name")
		except Group.DoesNotExist:
			pass
			
		return self.cleaned_data
			
class AddToGroupForm(forms.Form):
	user_list = forms.CharField(max_length=50,)
	#precisa de mais clean
	def clean(self):
		user_list=self.cleaned_data["user_list"]
		for username in user_list.split(" "):
			try:
				User.objects.get(username=username)
			except User.DoesNotExist:
				raise forms.ValidationError("User %s does not exist" % username)
				break
		
		return self.cleaned_data
