# Generated by Django 4.0.4 on 2022-06-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default='', max_length=30),
        ),
    ]
