from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

from .forms import EventForm, Enter_Question
from .models import *
from .utils import Calendar
from calendar import monthrange
from datetime import datetime,timedelta,date


# Create your views here.

def index(request):
    return HttpResponse('work already')

def question_enter(request):
  
    if request.POST:
        form = Enter_Question(request.POST)
        if form.is_valid():
            Question = form.cleaned_data['Question']
            form.save()
            return redirect('/')
    else:
        form = Enter_Question()
        return render(request,'questions.html',{'form':form})

class CalendarView(generic.ListView):
    model = Event
    template_name = 'diary/calendar.html'
    print(Event.title)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day',None))
        cal = Calendar(d.year,d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year,month = (int(x) for x in req_day.split('-'))
        return date(year,month,day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month='+str(prev_month.year)+'-'+str(prev_month.month)
    return month

def next_month(d):
    days_in_month = monthrange(d.year,d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month='+str(next_month.year)+'-'+str(next_month.month)
    return month

def event(request,event_id=None):
    question = Question.objects.all()
    random_items = random.choice(question)
    print(type(random_items))

    instance = Event()
    if event_id:
        instance = get_object_or_404(Event,pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)

    if request.POST and form.is_valid():
        form.save()
        question.save()
        return HttpResponseRedirect(reverse('diary:calendar'))
    return render(request,'diary/event.html',{'form':form,"question":str(question)})
