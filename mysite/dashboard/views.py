from django.http import HttpResponse
from .models import RewardFeed
from .models import Reward
from .models import JournalEntryList
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone


def index(request):
	latest_reward_list = RewardFeed.objects.order_by('-pub_date')[:5]
	latest_journal_list = JournalEntryList.objects.order_by('-pub_date')[:5]
	context = {
		'latest_reward_list': latest_reward_list,
		'latest_journal_list': latest_journal_list,
	}
	template = loader.get_template('dashboard/index.html')
	return render(request, 'dashboard/index.html', context)


def reward_detail(request, reward_id):	
	latest_reward_list = JournalEntryList.objects.order_by('-pub_date')[:5]
	reward = RewardFeed(reward_feed_text="congrats!", pub_date=timezone.now())
	for r in latest_reward_list:
		if reward_id == r.id:
			reward = r
	context = {
		'reward': reward,
	}
	template = loader.get_template('dashboard/reward.html')
	return render(request, 'dashboard/reward.html', context)

def reward_results(request, reward_id):
    response = "You're looking at the results of reward %s."
    return HttpResponse(response % reward_id)

def reward_vote(request, reward_id):
    return HttpResponse("You're voting on reward %s." % reward_id)


def journal_detail(request, journal_id):
	latest_journal_list = JournalEntryList.objects.order_by('-pub_date')[:5]
	journal = JournalEntryList(journal_entry_list_text="today was a good day", pub_date=timezone.now())
	for j in latest_journal_list:
		if journal_id == j.id:
			journal = j	
	context = {
		'journal_entry': journal,
	}
	template = loader.get_template('dashboard/journal.html')
	return render(request, 'dashboard/journal.html', context)

def journal_results(request, journal_id):
    response = "You're looking at the journal of reward %s."
    return HttpResponse(response % journal_id)

def journal_vote(request, journal_id):
    return HttpResponse("You're voting on journal %s." % journal_id)
