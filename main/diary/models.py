from django.db import models
from django.urls import reverse
from django import template

import datetime as dt
import random

# model
class Question(models.Model):
  Question = models.CharField(max_length=50)

  def __str__(self):
    return self.Question
class Event(models.Model):
    WTV = 'wtv'
    STFU = 'stfu'
    WTF = 'wtf'
    choices = [WTV,STFU,WTF]
    random_questions = [
        (WTV,'How are you today?'),
        (STFU,'what\'s up?'),
        (WTF,'How do you do?')
    ]

    title = models.CharField(max_length=50, choices=random_questions,default=random.choice(choices))
    description = models.TextField()
    start_time = models.DateTimeField(auto_now=dt.datetime.now())
    end_time = models.DateTimeField(auto_now=dt.datetime.now() + dt.timedelta(days=1))

    @property
    def get_html_url(self):
        url = reverse('diary:event_edit',args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'
    
    def __str__(self):
        return self.title



    