# Generated by Django 4.0.4 on 2022-06-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_name_signup_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone_number',
            field=models.ImageField(max_length=30, upload_to=''),
        ),
    ]