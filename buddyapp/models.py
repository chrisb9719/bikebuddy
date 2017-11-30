from __future__ import unicode_literals
from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    # Links UserProfile to a User model instance
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

"""class Comment(models.Model):
    route = models.ForeignKey('buddyapp.Route', related_name='comments',null=True)
    author = models.CharField(max_length=128, unique=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Rating(models.Model):
	RATING_CHOICES = (1,2,3,4,5
	route = models.ForeignKey('buddyapp.Route', related_name='ratings',null=True)
	author = models.CharField(max_length=128, unique=False)
	rating = models.IntegerField(choices=RATING_CHOICES, default=1)
	created_date = models.DateTimeField(default=timezone.now)
	approved_rating = models.BooleanField(default=False)

	def approve(self):
		self.approved_rating = True
		self.save()
	
	def __str__(self):
		return str(self.rating)
"""
# Configure a model for a playlist object
class Route(models.Model):

    name = models.CharField(max_length=128, unique=True)
    traffic = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    hillines = models.IntegerField(default=0)

    author = models.CharField(max_length=128, unique=False, blank=False)
	# Slug automatically generated
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
		### Code below is to help with testing
        if self.traffic < 0:
            self.traffic = 0
        if self.difficulty < 0 or self.rating > 5:
            self.difficulty = 0
        if self.views < 0:
            self.views = 0
        if self.rating < 0 or self.rating > 5:
            self.rating = 0
        if self.hilliness < 0:
            self.hilliness = 0
		###
        super(Route, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comment(models.Model):
    route = models.ForeignKey('buddyapp.Route', related_name='comments',null=True)
    author = models.CharField(max_length=128, unique=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



"""class Rating(models.Model):
    route = models.ForeignKey('buddyapp.Route', related_name='ratings',null=True)
    author = models.CharField(max_length=128, unique=False)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    created_date = models.DateTimeField(default=timezone.now)
    approved_rating = models.BooleanField(default=False)

    def approve(self):
        self.approved_rating = True
        self.save()

    def __str__(self):
        return str(self.rating)"""
