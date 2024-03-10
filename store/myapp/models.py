from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size)
    add_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

    class Meta:
        ordering = ['-add_date']

    def __str__(self) -> str:
        return self.name
    

