# Generated by Django 5.0.6 on 2024-06-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0020_cartitem_training_session_cartitem_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default='2024-01-01'),
        ),
    ]