# Generated by Django 5.0.6 on 2024-06-25 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0026_alter_ordertoproduct_training_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertoproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_product', to='coach.product'),
        ),
    ]
