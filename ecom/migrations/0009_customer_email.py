# Generated by Django 5.0.3 on 2024-03-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]