from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('',main_views.index,name='index'),
path('accounts/profile/',main_views.profile,name='profile'),
path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'),name='logout'),
path('register/',main_views.register,name='register'),
]

# if settings.DEBUG:
#   urlpatterns+= static(
#     settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
#   )
