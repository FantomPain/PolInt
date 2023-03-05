# Generated by Django 4.1.7 on 2023-03-05 21:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flowers', '0005_alter_basket_flower_id_alter_basket_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='basket',
            unique_together={('user', 'flower_id')},
        ),
    ]
