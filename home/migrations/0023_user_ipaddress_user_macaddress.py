# Generated by Django 4.0.4 on 2022-06-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ipaddress',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='macaddress',
            field=models.CharField(default='', max_length=30),
        ),
    ]