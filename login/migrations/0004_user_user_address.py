# Generated by Django 4.1.7 on 2023-03-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_user_name_user_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
