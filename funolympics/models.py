from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#This is the model for our venue
class Venue(models.Model):
    venueName = models.CharField(max_length=100)
    venueLocation = models.CharField(max_length=50, null=True)
    venueCapacity = models.PositiveSmallIntegerField(null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.venueName

    def save_venue(self):
        self.save()

    def delete_venue(self):
        self.delete()
