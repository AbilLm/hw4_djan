from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from product.models import Product, Comment, Category, Review


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
    return render(request, 'product/product_list.html', context)

def product_detail_view(request, pr_id):
    try:
        product = Product.objects.get(id=pr_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    comment = Comment.objects.get(id=1)
    print(product.comments.all())
    categories = product.categories.all()
    reviews = Review.objects.filter(product=product)

    context = {
        'product': product,
        'review': reviews,
        'categories': categories

    }

    return render(request, 'product/product_detail.html', context)



    return render(request, 'product/product_detail.html', context)

def category_page(request):
    categories = Category.objects.all()
    return render(request, 'product/category_page.html', {'categories': categories})