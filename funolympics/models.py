from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#This is the model for our venue
class Venue(models.Model):
    venueName = models.CharField(max_length=100)
    venueLocation = models.CharField(max_length=50, null=True)
    venueCapacity = models.PositiveSmallIntegerField(null=True)

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

#This is our model for facilities located in the venues.
class Facility(models.Model):
    facilityName = models.CharField(max_length=100)
    facilityLocation = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.CASCADE)
    facilityRoom = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.facilityName

    def save_facility(self):
        self.save()

    def delete_facility(self):
        self.delete()

#This is our model for blogs created by a user profile
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    venue = models.ForeignKey(Venue, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-postDate']

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()

    @classmethod
    def display_blogs(cls):
        blogs = cls.objects.all()
        return blogs

    @property
    def all_comments(self):
        return self.comments.all()

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	comment_id = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True,related_name='comments')
	status = models.CharField(max_length=2000)
	postDate = models.DateTimeField(auto_now_add=True)


#This is the model for our different sports available or supported in the venue
class Sport(models.Model):
    sportName = models.CharField(max_length=100)

    def __str__(self):
        return self.sportName

    def save_sport(self):
        self.save()

    def delete_sport(self):
        self.delete()

#This is our model for lessons available post olympics
class Lesson(models.Model):
    lessonName = models.CharField(max_length=100)
    lessonDescription = models.CharField(max_length=2000)
    lessonSport = models.ForeignKey(Sport, null=True, on_delete=models.CASCADE)
    lessonVenue = models.ForeignKey(Venue, null=True, on_delete=models.CASCADE)
    lessonFacility = models.ForeignKey(Facility, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.lessonName

    def save_lesson(self):
        self.save()


class schedule(models.Model):
    scheduleVenue = models.ForeignKey(Venue, null=True, on_delete=models.CASCADE)
    scheduleDate = models.DateTimeField(auto_now_add=True)
    scheduleFacility = models.ForeignKey(Facility, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.scheduleVenue


class Bookings(models.Model):
    lessonBooked = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE,related_name='booked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
