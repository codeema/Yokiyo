from django.urls import path,re_path
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
path('',main_views.index,name='index')
]

# if settings.DEBUG:
#   urlpatterns+= static(
#     settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
#   )