# Generated by Django 2.0.1 on 2018-04-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oslapp', '0013_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='oslapp.Profile'),
        ),
    ]
