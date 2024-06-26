# Generated by Django 5.0.6 on 2024-06-02 18:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50, null=True)),
                ('product_of_the_week', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart_name', models.CharField(max_length=255)),
                ('exp', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderToProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(through='coach.OrderToProduct', to='coach.product'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('urls', models.ImageField(upload_to='products/%y/%m/%d')),
                ('type', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.product')),
            ],
        ),
    ]
