# Generated by Django 2.0.1 on 2018-04-14 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oslapp', '0008_auto_20180414_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]