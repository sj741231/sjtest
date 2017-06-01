#-*- coding:utf-8 -*-
#from upload.models.py.bk import Profile
from upload.forms   import  ProfileForm
from django.shortcuts import render
#from somewhere import handle_uploader_file

'''

def saveprofile(request):
    saved= False
    
    if request.method == 'post':
        myprofileform = ProfileForm(request.POST,request.FILES)
        
        if myprofileform.is_valid():
            profile = Profile()
            profile.name = myprofileform.cleaned_data["name"]
            profile.file = myprofileform.cleaned_data["file"]
            profile.save()
            saved = True
    else:
        myprofileform = ProfileForm()

    return render(request, 'upload/saved.html', locals())

'''