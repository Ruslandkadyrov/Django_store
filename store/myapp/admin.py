from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, ProductSizeQty, Size, Category, Color, Subcategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_show', 'subcategory', "count", 'add_date']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None

    image_show.__name__ = 'Фото'


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(ProductSizeQty)
class ProductSizeQtyAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Subcategory, SubcategoryAdmin)
