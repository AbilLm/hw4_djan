from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product

def hello_view(request):
    return HttpResponse('Hello! Its my project')

def goodbye_view(request):
    return HttpResponse('Goodbye user!')

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def current_date_view(request):
    cur_time = datetime.now()
    return HttpResponse('Текущая дата и время: {}'.format(cur_time))

def product_list_view(request):
    products = Product.objects.all()
    context = {'product': products}
    return render(request, 'product_list.html', context)