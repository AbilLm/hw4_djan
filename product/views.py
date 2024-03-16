from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello_view(request):
    return HttpResponse('Hello! Its my project')

def goodbye_view(request):
    return HttpResponse('Goodbye user!')

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')

def current_date_view(request):
    cur_time = datetime.now()
    return HttpResponse('Текущая дата и время: {}'.format(cur_time))
