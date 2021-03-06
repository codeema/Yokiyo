from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views as main_views




urlpatterns = [
path('',main_views.index,name='index'),
path('accounts/profile/',main_views.profile,name='profile'),
path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'),name='logout'),
path('register/',main_views.register,name='register'),
path('post/',main_views.post,name='post'),
path('news/',main_views.news,name='news'),
path('lesson/',main_views.subscription,name='lesson'),
path('venue/',main_views.venues,name='venue'),
path('sport/',main_views.sport,name='sport  '),
path('schedule/',main_views.schedules,name='schedule'),
re_path(r'^comment/(?P<blog_id>\d+)$',main_views.commenting,name='commenting'),
re_path(r'^booking/(?P<lesson_id>\d+)$',main_views.booking,name='booking'),
path('mybookings/',main_views.my_booking,name='my_bookings'),
re_path(r'^index/blog/(?P<blog_id>\d+)$',main_views.specific_blog,name='specific_blog'),
]

# if settings.DEBUG:
#   urlpatterns+= static(
#     settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
#   )
