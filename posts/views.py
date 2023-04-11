from django.shortcuts import HttpResponse
import datetime

# Create your views here.

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my project')

def now_date(request):
    if request.method == 'GET':
        current_date = datetime.datetime.now()
        return HttpResponse(f'Today is {current_date}')

def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye, user')

