from django.contrib import admin

# Register your models here.
from product.models import Product, Comment, Category, Tag, Review

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)