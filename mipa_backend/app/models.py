# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=100)
    category = models.TextField()
    difficulty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)

class Question(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='questions', on_delete=None)
    kind = models.CharField(max_length=100)
    question = models.TextField()
    code = models.TextField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    solution = models.TextField()
    hint = models.TextField(blank=True, null=True)    
    category = models.CharField(max_length=200)
    questionImage = models.CharField(max_length=300, blank=True, null=True)
    hintImage = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('created_at',)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    current_score = models.IntegerField(blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()   

class ChallengeCompletion(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    points_received = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)