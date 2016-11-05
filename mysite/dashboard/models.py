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

class RewardFeed(models.Model):
    reward_feed_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Reward(models.Model):
    rewardfeed = models.ForeignKey(RewardFeed, on_delete=models.CASCADE)
    reward_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class ActivityFeed(models.Model):
    activity_feed_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Activity(models.Model):
    activityfeed = models.ForeignKey(ActivityFeed, on_delete=models.CASCADE)
    activity_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class JournalEntryList(models.Model):
    journal_entry_list_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class JournalEntry(models.Model):
    journalentrylist = models.ForeignKey(JournalEntryList, on_delete=models.CASCADE)
    journal_entry_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
