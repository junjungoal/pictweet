from django.conf.urls import patterns, url
from tweets import views

urlpatterns = patterns('',
  url(r'^tweets/$', views.tweet_list, name='tweet_list')
)
