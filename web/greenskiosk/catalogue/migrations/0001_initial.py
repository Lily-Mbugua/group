# Generated by Django 3.1.1 on 2020-09-24 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kiosks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=100)),
                ('supplier_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('number_in_stock', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('street_address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('id_number', models.IntegerField()),
                ('date_added', models.DateField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='kiosk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiosks.kiosk'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.product_supplier'),
        ),
    ]
