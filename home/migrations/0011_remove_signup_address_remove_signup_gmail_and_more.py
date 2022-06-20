# Generated by Django 4.0.4 on 2022-06-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_user_city_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='address',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='name',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='signup',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
