#coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book
from django.http.response import HttpResponseRedirect
from django.template import RequestContext
import sjform


def search_form(request):
    '''
    访问表单查询，使用get方式，配合func search
    '''
    return render_to_response('sjform/search_form.html')

'''
def search(request):
    if 'q' in request.GET and request.GET['q']:
#        message = 'You searched for: %r' % request.GET['q']
        q_value = request.GET['q']
        books = Book.objects.filter(title__icontains = q_value)
        return render_to_response('sjform/search_results.html',{ 'books':books, 'query':q_value})
        
    else:
        return HttpResponse('You submitted an query')
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)
'''

def search(request):
    '''
    通过GET方式获取输入参数，通过数据对象在数据库中查询参数
    '''
    if 'q' in request.GET and request.GET['q']:
        q_value = request.GET['q']
        books = Book.objects.filter(title__icontains = q_value)
        return render_to_response('sjform/search_results.html', {'books':books, 'query':q_value})
    else:
        return render_to_response('sjform/search_form.html', {'error': True})
'''    
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')
        if not request.POST.get('message',''):
            errors.append('Enter message')
        if not request.POST.get('email') and '@' in request.POST['email']:
            errors.append('Enter a valid email')
    
    subject_value = request.POST.get('subject')
    email_value = request.POST.get('email')
    message_value = request.POST.get('message')
'''    


def record_form(request):
    '''
    返回表单，POST方式
    '''
    return render_to_response('sjform/record_form.html',context_instance=RequestContext(request))

def record(request):
    '''
    1.检查填入参数是否合规
    2.合规后，创建数据对象并存入数据库，返回成功页
    3.如果不合规，返回当前页重填，之前参数自动带入
    '''
    errors = []
    if request.method == 'POST':
        if not request.POST.get('title',''):
            errors.append('Enter  title')
        if not request.POST.get('author',''):
            errors.append('Enter author')
        if not request.POST.get('pubisher'):
            errors.append('Enter  pubisher')
    
    if not errors:
        b = Book.objects.create(title=request.POST.get("title"), 
                                author=request.POST.get("author"),
                                pubisher=request.POST.get("pubisher")
                                ) 
        return HttpResponseRedirect("/sjform/thanks/")
    
    
    return render_to_response('sjform/record_form.html',{'errors': errors,
                                                        'title': request.POST.get("title"),
                                                        'author': request.POST.get("author"),
                                                        'pubisher': request.POST.get("pubisher")},
                                                        context_instance=RequestContext(request))
    

def thanks(request):
    '''
    录入数据成功页
    '''
    return render_to_response('sjform/thanks.html')