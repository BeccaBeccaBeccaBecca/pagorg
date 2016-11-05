from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reward/(?P<reward_id>[0-9]+)/$', views.reward_detail, name='reward_detail'),
    url(r'^journal/(?P<journal_id>[0-9]+)/$', views.journal_detail, name='journal_detail'),
]