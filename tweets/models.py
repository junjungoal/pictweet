from django.db import models

class Tweet(models.Model):
  text = models.TextField(u'ツイート内容')
  image = models.TextField(u'画像')

  def __str__(self):
    return  self.text
