# Generated by Django 5.0.6 on 2024-06-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_datetime_created_book_datetime_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=False),
        ),
    ]