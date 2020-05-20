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

#This is our model for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='profilepic/')
    currentLocation = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=254)
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
