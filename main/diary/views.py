from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView 
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.utils.safestring import mark_safe

from .forms import *
from .models import *
from .utils import Calendar

from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse('work already')

def Enter_Question(request):
  
    if request.method == 'POST':
        form = Enter_Question(request.POST)
    
        question = form.cleaned_data['Question']
        form.save()
        return redirect('index')
    else:
        form = Enter_Question()
        return render(request,'questions.html',{'form':form})

class CalendarView(generic.ListView):
    model = Event
    template_name = 'diary/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day',None))
        cal = Calendar(d.year,d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year,month = (int(x) for x in req_day.split('-'))
        return date(year,month,day=1)
    return datetime.today()


