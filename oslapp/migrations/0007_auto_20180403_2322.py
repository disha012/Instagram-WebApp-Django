# Generated by Django 2.0.1 on 2018-04-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oslapp', '0006_auto_20180403_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.FileField(null=True, upload_to='document/'),
        ),
    ]