# Generated by Django 3.2.8 on 2023-05-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20230429_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='download',
            field=models.BooleanField(default=False),
        ),
    ]