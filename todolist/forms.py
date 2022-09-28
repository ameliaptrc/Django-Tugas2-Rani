from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    description = forms.CharField(label ='Description',widget= forms.Textarea, required=False)