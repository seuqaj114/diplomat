import dbus
import os
import psutil
import time
import json
from httplib2 import Http
import urllib2 as url2
import urllib
import requests

item              = "org.freedesktop.Notifications"
path              = "/org/freedesktop/Notifications"
interface         = "org.freedesktop.Notifications"
app_name          = "Test Application"
id_num_to_replace = 0
icon              = "/home/miguel/Documents/Python/notify/icon.png"
title             = "New file open"
actions_list      = ''
hint              = ''
duration = 2

running=[]

def warning(file_path):
	text = file_path+" was just opened."
	bus = dbus.SessionBus()
	notif = bus.get_object(item, path)
	notify = dbus.Interface(notif, interface)
	notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, duration)

def post_open(file_path,username):
	content={"name":file_path,
			"user":{"username":username}}
	requests.post(
					url='http://localhost:8000/api/v1/open/',
					data=json.dumps(content),
					headers={'content-type':'application/json'},
	)
	
def delete_open(file_path,username):
	
	requests.delete("http://localhost:8000/api/v1/open/?user__username="+username+"&name="+file_path.replace("#","%23"))
	
	"""
	req = requests.get("http://localhost:8000/api/v1/open/?user__username="+username)
	data = req.json()
	for item in data["objects"]:
		if item["name"] == file_path:
			requests.delete("http://localhost:8000/api/v1/open/%s/" % item["id"])
			break
	"""
	

"""
while(1):
	f=os.popen("ps auxww")
	now=[]
	print "Processes:"	
	for line in f:
		if "Dropbox" in line:
			filename=line.split("/")[-1]
			#print filename
			procid=line.split()[1]
			print procid
			now.append([filename,procid])
		
	match = [x for x in now if x in running]
	print "Running:"
	print running
	print "Match:"
	print match
	print "Now:"
	print now

	response = url2.urlopen("http://127.0.0.1:8000/api/open/?format=json")
	data = response.read()
	res = json.loads(data)
	#print "Data in server:"
	#for item in res["objects"]:
	#	print item["name"]

	for x in running:
		if x not in match:
			running.remove(x)
			temp_url="http://localhost:8000/api/open/?name="+x[0]
			requests.delete(temp_url)
	for x in now:
		if x not in match:
			running.append(x)
			requests.post(
						url='http://localhost:8000/api/open/',
						data=json.dumps({"name":x[0]}),
						headers={'content-type':'application/json'},
			)

			#Notification
			text = x[0]+" was just opened."
			bus = dbus.SessionBus()
			notif = bus.get_object(item, path)
			notify = dbus.Interface(notif, interface)
			notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, duration)

	print "Running2:"
	print running

	time.sleep(5)




#Config



#Notification
bus = dbus.SessionBus()
notif = bus.get_object(item, path)
notify = dbus.Interface(notif, interface)
notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, duration)

f.close()
#time.sleep(10)

"""
