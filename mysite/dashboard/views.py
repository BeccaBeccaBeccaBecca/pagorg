from django.shortcuts import render
from django.utils import timezone

from .models import RewardFeed, JournalEntryList


def index(request):
    latest_reward_list = RewardFeed.objects.order_by('-pub_date')[:5]
    latest_journal_list = JournalEntryList.objects.order_by('-pub_date')[:5]
    context = {
    	'latest_reward_list': latest_reward_list,
    	'latest_journal_list': latest_journal_list
    	}

    return render(request, 'dashboard/index.html', context)


def reward_detail(request, reward_id):
	latest_reward_list = RewardFeed.objects.order_by('-pub_date')[:5]
	reward = RewardFeed(reward_feed_text="congrats!", pub_date=timezone.now())
	for r in latest_reward_list:
		if r.id == reward_id:
			reward = r
	
	context = {
    	'reward': reward
    	}

	return render(request, 'dashboard/reward.html', context)

def journal_detail(request, journal_id):
	latest_journal_list = JournalEntryList.objects.order_by('-pub_date')[:5]
	journal = JournalEntryList(journal_entry_list_text="Today was a good day!", pub_date=timezone.now())
	for j in latest_journal_list:
		if j.id == journal_id:
			journal = j
    
	context = {
    	'journal': journal
    	}

	return render(request, 'dashboard/journal.html', context)
