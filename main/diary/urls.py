from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r"^enter_question/$",views.question_enter,name='question_enter'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), 
    url(r'^$',views.event,name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    
]
