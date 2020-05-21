from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Venue, Sport, Profile, Blog, Location, Facility, Comment

#This is a sign up form for creating a user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewVenueForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('venueName', 'venueLocation', 'venueCapacity', 'admin')

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['venue', 'user']
        fields = ('venueName', 'venueLocation', 'venueCapacity', 'admin')

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email_confirmed']

class NewFacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        exclude = ['venue', 'user']

class NewSportForm(forms.ModelForm):
    class Meta:
        model = Sport
        exclude = ['venue', 'user']

class NewCommentForm(forms.ModelForm):
	class Meta:
        model = Comment
        exclude = ['venue', 'user']
		
