# Generated by Django 3.2.8 on 2023-04-26 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consecutive', models.IntegerField()),
                ('code', models.IntegerField()),
                ('product', models.CharField(max_length=150)),
                ('quanty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
