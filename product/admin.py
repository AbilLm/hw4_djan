from django.contrib import admin

# Register your models here.
from product.models import Product, Comment, Category, Tag, Review


# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'id')
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'tags')
        }),
        ('Readonly Fields', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })

    )


#admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'text')
    readonly_fields = ('text', 'product')



#admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    readonly_fields = ('name', 'description')

#admin.site.register(Tag)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


#admin.site.register(Review)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'created_at')
    readonly_fields = ('rating', 'created_at')
