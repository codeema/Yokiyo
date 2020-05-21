from django.shortcuts import render, redirect
from .models import Profile, Blog, Facility, Lesson, Sport
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
# from .forms import SignUpForm, NewBusinessForm, NewPostForm, EditProfile, NewHoodForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    '''
    View function that displays the homepage and all its contents including social ammenitits and hoods notices
    '''
    blog = Blog.objects.all()
    facility = Facility.objects.all()
    sport = Sport.objects.all()
    lesson = Lesson.objects.all()
    return render(request, 'index.html' )

# {"facility": facility,"blog": blog[::-1], "sport": sport[::-1], "lesson":lesson}