# Generated by Django 3.2.8 on 2023-04-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_consecutive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='consecutive',
            field=models.IntegerField(),
        ),
    ]
