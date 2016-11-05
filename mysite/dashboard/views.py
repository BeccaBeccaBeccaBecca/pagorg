from django.shortcuts import render
from django.utils import timezone

from .models import RewardFeed, JournalEntryList, Badge


def index(request):
	badge = Badge(name="congrats!")
	latest_badge_list = Badge.objects.order_by('-create_dt')[:5]
	latest_journal_list = JournalEntryList.objects.order_by('-pub_date')[:5]
	points = calculate_all_points
	context = {
    	'user': "me!",
    	'points': points,
    	'latest_badge_list': latest_badge_list,
    	'latest_journal_list': latest_journal_list
    	}

	return render(request, 'dashboard/Dashboard.html', context)


def reward_detail(request, reward_id):
	latest_badge_list = Badge.objects.order_by('-create_dt')[:5]
	badge = Badge(name="congrats!")
	for b in latest_badge_list:
		if b.id == reward_id:
			badge = b
	
	context = {
    	'badge': badge
    	}

	return render(request, 'dashboard/badge.html', context)

def journal_detail(request, journal_id):
	latest_journal_list = JournalEntryList.objects.order_by('-pub_date')[:5]
	journal = JournalEntryList(journal_entry_list_text="Today was a good day!", pub_date=timezone.now())
	for j in latest_journal_list:
		if j.id == journal_id:
			journal = j
    
	context = {
    	'journal_entry': journal
    	}

	return render(request, 'dashboard/journal.html', context)


def calculate_all_points():
	return 10
