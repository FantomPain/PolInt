# Generated by Django 4.1.7 on 2023-03-26 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0011_rename_flower_id_basket_flower_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimagemodel',
            name='name',
        ),
    ]
