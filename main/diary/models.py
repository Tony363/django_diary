from django.db import models
from django.urls import reverse
import datetime as dt

# Create your models here.
class Question(models.Model):
    ID = models.IntegerField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    Question = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.Question
    @property
    def get_html_url(self):
        url = reverse('event_edit',args=(self.id))
        return f'<p>{self.Question}</p><a href="{url}">edit</a>'


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now=dt.datetime.now())
    end_time = models.DateTimeField(auto_now=dt.datetime.now() + dt.timedelta(days=1))

    @property
    def get_html_url(self):
        url = reverse('diary:event_edit',args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'



    