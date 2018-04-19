'''from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
'''
from __future__ import unicode_literals
from vote.models import VoteModel
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    # follows = models.ManyToManyField('Profile', related_name='followed_by', symmetrical=False, blank=True)
    # dp = models.FileField(null=True, upload_to='user/')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


'''
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
'''


class Document(VoteModel, models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='document/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


'''
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    picture = models.ForeignKey(Document, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    followed = models.ForeignKey(User, related_name='followed')
    follower = models.ForeignKey(User, related_name='followers')
'''
