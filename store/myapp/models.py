from django.utils import timezone
from django.db import models
import uuid
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, default=uuid.uuid4)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(null=True, default=uuid.uuid4)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=10)
    slug = models.SlugField(null=True, default=uuid.uuid4)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)
    sizes = models.ManyToManyField(Size)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-add_date']

    def __str__(self) -> str:
        return self.name


class ProductSizeQty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size_qty')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True, default=uuid.uuid4)


@receiver(post_save, sender=ProductSizeQty)
def add_sizes_to_product(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        size = instance.size
        product.sizes.add(size)


@receiver(pre_delete, sender=ProductSizeQty)
def remove_sizes_from_product(sender, instance, **kwargs):
    product = instance.product
    size = instance.size
    product.sizes.remove(size)


@receiver(post_delete, sender=ProductSizeQty)
def remove_unused_sizes(sender, instance, **kwargs):
    size = instance.size
    if not ProductSizeQty.objects.filter(size=size).exists() and not Product.objects.filter(sizes=size).exists():
        size.delete()
