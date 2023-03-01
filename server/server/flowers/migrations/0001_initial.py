# Generated by Django 4.1.7 on 2023-02-27 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('percent', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.sale')),
            ],
        ),
    ]
