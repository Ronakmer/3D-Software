# Generated by Django 4.0.4 on 2022-06-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_signup_address_remove_signup_gmail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(default='', max_length=300),
        ),
    ]