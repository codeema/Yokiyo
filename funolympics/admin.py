from django.contrib import admin
from .models import Venue, Profile, Facility, Blog, Sport, Lesson, schedule

# Register your models here.
admin.site.register(Venue)
admin.site.register(Profile)
admin.site.register(Facility)
admin.site.register(Blog)
admin.site.register(Sport)
admin.site.register(Lesson)
admin.site.register(schedule)