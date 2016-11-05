from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckInEntry(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	feeling = models.CharField(max_length=255,blank=True, null=True)
	need = models.CharField(max_length=255, blank=True, null=True)
	points = models.IntegerField(default=1)
	public = models.BooleanField(default=0)
	create_dt = models.DateTimeField(auto_now_add=True)

class JournalEntry(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	checkIn = models.ForeignKey(CheckInEntry, blank=True, null=True)
	text = models.TextField(max_length=10000)
	points = models.IntegerField(default=1)
	create_dt = models.DateTimeField(auto_now_add=True)
