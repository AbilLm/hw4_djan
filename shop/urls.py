"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('shop/', include('shop.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import hello_view, category_page
from product.views import goodbye_view
from product.views import main_page_view
from product.views import current_date_view
from product.views import product_list_view
from product.views import product_detail_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('', main_page_view),
    path('goodbye/', goodbye_view),
    path('current_date/', current_date_view),
    path('products/', product_list_view),
    path('products/<int:pr_id>/', product_detail_view),
    path('categories', category_page),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)