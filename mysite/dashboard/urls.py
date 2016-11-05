from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^reward/(?P<reward_id>[0-9]+)/$', views.reward_detail, name='reward_detail'),
    # ex: /polls/5/results/
    url(r'^reward/(?P<reward_id>[0-9]+)/results/$', views.reward_results, name='reward_results'),
    # ex: /polls/5/vote/
    url(r'^reward/(?P<reward_id>[0-9]+)/vote/$', views.reward_vote, name='reward_vote'),

    url(r'^journal/(?P<journal_id>[0-9]+)/$', views.journal_detail, name='journal_detail'),
    # ex: /polls/5/results/
    url(r'^journal/(?P<journal_id>[0-9]+)/results/$', views.journal_results, name='journal_results'),
    # ex: /polls/5/vote/
    url(r'^journal/(?P<journal_id>[0-9]+)/vote/$', views.journal_vote, name='journal_vote'),
]