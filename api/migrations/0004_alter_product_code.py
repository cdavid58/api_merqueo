# Generated by Django 3.2.8 on 2023-04-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
