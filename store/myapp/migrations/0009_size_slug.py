# Generated by Django 4.2.7 on 2024-03-16 09:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_category_slug_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, null=True),
        ),
    ]
