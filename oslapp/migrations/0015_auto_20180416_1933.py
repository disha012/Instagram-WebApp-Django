# Generated by Django 2.0.1 on 2018-04-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oslapp', '0014_profile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='document',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='oslapp.Profile'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
