# Generated by Django 3.2.8 on 2023-04-27 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('product', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='Product')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
            ],
        ),
    ]
