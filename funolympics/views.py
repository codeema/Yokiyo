from django.shortcuts import render, redirect
from .models import Profile, Blog, Facility, Lesson, Sport, Comment
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import RegistrationForm, NewVenueForm, NewBlogForm, EditProfile, NewFacilityForm, NewSportForm, NewCommentForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,Welcome ')
      return redirect('login')
  else:
    form = RegistrationForm()
  return render(request,'registration.html',{"form":form})

def index(request):
    '''
    View function that displays the homepage and all its contents including social ammenitits and hoods notices
    '''
    blog = Blog.objects.all()
    facility = Facility.objects.all()
    sport = Sport.objects.all()
    lesson = Lesson.objects.all()
    return render(request, 'index.html',{"facility": facility,"blog": blog[::-1], "sport": sport[::-1], "lesson":lesson} )


# profile view

@login_required
def profile(request):
  current_user = request.user
  
  return render(request,'profile.html',{"current_user":current_user})

