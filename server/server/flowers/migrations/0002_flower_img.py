# Generated by Django 4.1.7 on 2023-02-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
