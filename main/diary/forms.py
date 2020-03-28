from django import forms
from .models import *

class Enter_Question(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ['Question']
    
    def save(self,commit=True):
        user = super(Enter_Question,self).save(commit=False)
        user.Question = self.cleaned_data['Question']
        if commit:
            user.save()
        return user

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # widgets = {
        #     'start_time': forms.DateInput(attrs={'type':'datetime-local'},format='%Y-%m-%d'),
        #     'end_time': forms.DateInput(attrs={'type': 'datetime-local'},format='%Y-%m-%d'),
        # }
        fields = '__all__'
    
    def __init__(self,*args,**kwargs):
        super(EventForm,self).__init__(*args,**kwargs)
        # self.fields['start_time'].input_formats = ('%Y-%m-%d',)
        # self.fields['end_time'].input_formats = ('%Y-%m-%d',)
        
    