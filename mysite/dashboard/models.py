from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Badge(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	name = models.CharField(max_length=255,)
	image = models.CharField(max_length=255, blank=True, null=True)
	create_dt = models.DateTimeField(auto_now_add=True)
