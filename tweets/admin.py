from django.contrib import admin
from tweets.models import Tweet

# admin.site.register(Tweet)

class TweetAdmin(admin.ModelAdmin):
  list_display = ('id', 'text', 'image')
  list_display_links = ('id', 'text')

admin.site.register(Tweet, TweetAdmin)
