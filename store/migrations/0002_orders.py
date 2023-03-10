# Generated by Django 4.1.7 on 2023-03-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_firstname', models.CharField(max_length=100)),
                ('order_lastname', models.CharField(max_length=100)),
                ('order_email', models.CharField(max_length=100)),
                ('order_address', models.CharField(max_length=200)),
                ('order_country', models.CharField(max_length=200)),
                ('order_city', models.CharField(max_length=200)),
                ('order_zip', models.CharField(max_length=6)),
                ('order_products', models.CharField(max_length=500)),
            ],
        ),
    ]
