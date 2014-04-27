from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

#AINDA NAO ESTA PREPARADO PARA PARTILHA DE PASTAS INTERIORES
#Sera necessario extender o Group
class Open(models.Model):
	name = models.TextField()
	open_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return "%s - %s" % (self.name,self.opened)

	class Meta:
		ordering = ('open_date',)

#melhorar a organizacao deste model! passar para foreign keys ou parecido
class Invitation(models.Model):
	group_id = models.IntegerField()
	sender_id = models.IntegerField()
	invitation_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	
	class Meta:
		ordering = ('invitation_date',)
	
class Folder(models.Model):
	name = models.TextField(blank=True)
	path = models.TextField()
	users = models.ManyToManyField(User)
	
	def __unicode__(self):
		return "%s - %s" % (self.name,self.path)
		
	def create_name(self):
		self.name = self.path.split("/")[-1]
		
	class Meta:
		ordering = ('name',)
