from django.contrib import admin

from .models import Product, Size, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'category', "count", 'add_date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Category)
