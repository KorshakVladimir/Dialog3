# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class GameList(models.Model):
    title = models.CharField(max_length=255) # заголовок

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/games/%i/" % self.id

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=False) #TJ {10.05.2015} unique=True - должно быть, но дает error
#    profile_picture = models.ForeignKey(Picture, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True, choices=(("Male", "Male"), ("Female", "Female")))
    #spoken_languages = models.CharField(max_length=150, null=True, blank=True)
    #hometown = models.CharField(max_length=40, null=True, blank=True)
    #home_country = models.CharField(max_length=25, null=True, blank=True)
    #home_state = models.CharField(max_length=30, null=True, blank=True)
    #current_town = models.CharField(max_length=40, null=True, blank=True)
    #current_country = models.CharField(max_length=25, null=True, blank=True)
    #current_state = models.CharField(max_length=30, null=True, blank=True)
    #friends = models.ManyToManyField(User, null=True, blank=True, related_name='friends')
    #subscriptions = models.ManyToManyField(User, null=True, blank=True, related_name='subscriptions')
    #invites = models.ManyToManyField(Invite, null=True, blank=True, related_name='invites')
    #event_invites = models.ManyToManyField(EventInvite, null=True, blank=True, related_name='event_invites')
    #albums = models.ManyToManyField(Album, null=True, blank=True)
    #events = models.ManyToManyField(Event, null=True, blank=True)
    #relationship_status = models.ForeignKey(Relationship, null=True, blank=True)
    #schools = models.ManyToManyField(School, through=SchoolMembership, null=True, blank=True)
    #employers = models.ManyToManyField(Employer, through=EmployerMembership, null=True, blank=True)
    #messages = models.ManyToManyField(Message, null=True, blank=True)
    #comments = models.ManyToManyField(Comment, null=True, blank=True)
    #groups = models.ManyToManyField(Group, null=True, blank=True)
    #site_language = models.ForeignKey(Language, null=True, blank=True)
    url = models.CharField(max_length=20, unique=True)
    # color_bottom = models.CharField(max_length=20)
    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

from cgm import util
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        user = kwargs.get('instance')
        url = util.gen_url()
        UserProfile.objects.create(user=user, url=url)

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)