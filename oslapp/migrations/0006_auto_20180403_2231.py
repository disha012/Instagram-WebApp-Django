# Generated by Django 2.0.1 on 2018-04-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oslapp', '0005_auto_20180401_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.AddField(
            model_name='profile',
            name='dp',
            field=models.FileField(null=True, upload_to='usersdp/'),
        ),
    ]
