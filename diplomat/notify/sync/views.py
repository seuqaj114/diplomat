from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from sync.forms import LoginForm, RegisterForm, NewGroupForm, AddToGroupForm
from sync.models import *
# Create your views here.

#def is_not_logged(user):
#	return not user.is_authenticated()


#@user_passes_test(is_not_logged,login_url="home:profile")
def start(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect(reverse("home:profile"))
	
	return render(request,"sync/start.html",{})
	
def login(request):
	if request.method == "POST":
		loginform=LoginForm(request.POST)
		if loginform.is_valid():
			cd=loginform.cleaned_data
			user=auth.authenticate(username=cd["username"],password=cd["password"])
			auth.login(request,user)
			return HttpResponseRedirect(reverse("home:profile"))
	else:
		loginform=LoginForm()

	return render(request,"sync/login.html",{"loginform":loginform})
	
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse("home:start"))
	
def register(request):
	if request.method == "POST":
		registerform=RegisterForm(request.POST)
		if registerform.is_valid():
			cd=registerform.cleaned_data
			User.objects.create_user(username=cd["username"],password=cd["password"])
			user=auth.authenticate(username=cd["username"],password=cd["password"])
			auth.login(request,user)
			return HttpResponseRedirect(reverse("home:profile"))
	else:
		registerform=RegisterForm()
		
	return render(request,"sync/register.html",{"registerform":registerform})

@login_required(login_url="home:login")
def profile(request):

	return render(request,"sync/profile.html",{})
	
@login_required(login_url="home:login")
def groups(request):

	return render(request,"sync/groups.html",{})
	
@login_required(login_url="home:login")
def new_group(request):
	if request.method == "POST":
		newgroupform = NewGroupForm(request.user,request.POST)
		if newgroupform.is_valid():
			cd=newgroupform.cleaned_data
			new_group = Group.objects.create(name=cd["name"])
			request.user.groups.add(new_group)
			return HttpResponseRedirect(reverse("home:groups"))
	else:
		newgroupform=NewGroupForm(request.user)
		
	return render(request,"sync/new_group.html",{"newgroupform":newgroupform})
	
@login_required(login_url="home:login")
def add_to_group(request):
	if request.method == "POST":
		addtogroupform = AddToGroupForm(request.POST)
		if addtogroupform.is_valid():
			cd = addtogroupform.cleaned_data
			username_list = cd["user_list"].split(" ")
			users = [User.objects.get(username=username) for username in username_list]
			print users
			for key, value in request.POST.iteritems():
				if "check" in key:
					for user in users:
						user.invitation_set.create(group_id=value,sender_id=request.user.id)
					#print value
					#group = Group.objects.get(pk=value).user_set.add(*users)
			return HttpResponseRedirect(reverse("home:groups"))
					
	else:
		addtogroupform=AddToGroupForm()
	
	return render(request,"sync/add_to_group.html",{"addtogroupform":addtogroupform})

@login_required(login_url="home:login")
def accept_invitation(request,inv_id):
	invitation = Invitation.objects.get(pk=inv_id)
	group = Group.objects.get(pk=invitation.group_id)
	group.user_set.add(request.user)
	invitation.delete()
	
	return HttpResponseRedirect(reverse("home:groups"))
	
