from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=50)
    dev_name = models.CharField(max_length=50)
    brief_desc = models.TextField()
    owner = models.ForeignKey(User, related_name='dev_rooms' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MainSilo(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True) # Room ID + RoomLink Name + 'silo'

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        mainsilo = cls(name=name)
        return mainsilo

class AuxSilo(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True)
    data = models.TextField(default=None, blank=True)
    link = models.CharField(max_length=100, default=None, blank=True, null=True)
    time = models.DateTimeField(default=None, blank=True, null=True)
    data_hash = models.TextField(default=None, blank=True, null=True)

class RoomLink(models.Model):
    display_name = models.CharField(max_length=70, default=None)
    name = models.CharField(max_length=70,default=None, blank=True,)
    desc = models.TextField(default="")
    users = models.ManyToManyField('accounts.Profile', related_name='mylinks', default=None, blank=True)
    room = models.ForeignKey(Room, related_name='links', on_delete=models.CASCADE)
    sought = models.BooleanField(default=False)
    buyers = models.ManyToManyField(User, related_name='mybuyers', default=None, blank=True)
    call_time = models.PositiveIntegerField(default=None, blank=True, null=True)
    fields = models.TextField(default=None, null=True)
    off_id = models.TextField(default=None, null=True, blank=True) #  The id for the room link when the process is handled by the company
    data_needed = models.BooleanField(default=False) #  This indicates whether this needs data from the device or from the server (only if off_id is not None)
    url = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

"""
class LinkRegData(models.Model):
    name = models.CharField(max_length=70, default=None, primary_key=True)
    data = models.TextField(default=None)

    def __str__(self):
        return self.name
"""

class LinkRegularData(models.Model):
    name = models.CharField(max_length=70, default=None)
    data = models.TextField(default=None)

    def __str__(self):
        return self.name
