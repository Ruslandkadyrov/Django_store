from django.contrib import admin

from .models import Product, Size, Category, Color, Subcategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'subcategory', "count", 'add_date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Subcategory)