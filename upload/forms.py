#-*- coding: utf-8 -*-
from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length = 100)
    file = forms.FileField()
    
    
class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()