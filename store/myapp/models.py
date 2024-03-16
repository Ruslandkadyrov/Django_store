from django.utils import timezone
from django.db import models
import uuid


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


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)
    sizes = models.ManyToManyField(Size)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1)
    add_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

    class Meta:
        ordering = ['-add_date']

    def __str__(self) -> str:
        return self.name
