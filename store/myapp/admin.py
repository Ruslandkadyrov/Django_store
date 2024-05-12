from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, ProductSizeQty, Size, Category, Subcategory


class ProductSizeQtyInline(admin.TabularInline):
    model = ProductSizeQty
    exclude = ('slug',)
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_show', 'subcategory', 'sizes_and_quantities', 'add_date']
    list_editable = ["price"]
    search_fields = ["name"]
    list_filter = ['subcategory']
    exclude = ('sizes',)

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None
    image_show.__name__ = 'Фото'
    inlines = [ProductSizeQtyInline]

    def sizes_and_quantities(self, obj):
        sizes_and_quantities = ""
        for size_qty in obj.product_size_qty.all():
            sizes_and_quantities += f"{size_qty.size}/{size_qty.quantity}, "
        return sizes_and_quantities
    sizes_and_quantities.short_description = 'Sizes/Quantities'


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(ProductSizeQty)
class ProductSizeQtyAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Subcategory, SubcategoryAdmin)
