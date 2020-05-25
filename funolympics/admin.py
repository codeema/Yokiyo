from django.contrib import admin
from .models import Venue, Profile, Facility, Blog, Sport, Lesson, Booking, schedule, Comment

# Register your models here.
admin.site.register(Venue)
admin.site.register(Profile)
admin.site.register(Facility)
admin.site.register(Blog)
admin.site.register(Sport)
admin.site.register(Lesson)
admin.site.register(Booking)
admin.site.register(schedule)
admin.site.register(Comment)
