from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Venue, Sport, Profile, Blog, Facility, Comment

# Location

# User Creation Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Venue Creation Form
class NewVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('venueimage','venueName', 'venueLocation', 'venueCapacity')

# Blog Creation Form
class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['venue', 'user']
       

# Profile Creation Form
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email_confirmed']

# Facility Creation Form
class NewFacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        exclude = ['venue', 'user']

# Sport Creation Form
class NewSportForm(forms.ModelForm):
    class Meta:
        model = Sport
        exclude = ['venue', 'user']

# Comment Creation Form
class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['venue', 'user','comment_id']
		
