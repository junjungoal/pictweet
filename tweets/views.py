from django.shortcuts import render
from django.http import HttpResponse

def tweet_list(request):
  return HttpResponse(u'書籍の一覧')