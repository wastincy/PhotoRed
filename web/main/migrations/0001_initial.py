# Generated by Django 4.0.3 on 2022-03-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='id')),
                ('login', models.CharField(max_length=30, verbose_name='login')),
                ('password', models.CharField(max_length=30, verbose_name='password')),
            ],
        ),
    ]