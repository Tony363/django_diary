from django import forms
from .models import *

class Enter_Question(forms.ModelForm):
    
    class Meta():
        model = Question
        fields = ['Question']
    
    def save(self,commit=True):
        user = super(Enter_Question,self).save(commit=False)
        user.Question = self.cleaned_data['Question']
        if commit:
            user.save()
        return user
    