# Generated by Django 2.0.1 on 2018-04-01 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oslapp', '0004_auto_20180401_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]