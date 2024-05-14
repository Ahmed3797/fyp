from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
 path("<id>",views.Interview.as_view(),name="interview"),
 path('save_answers/', views.save_answers, name='save_answers'),
#  path('webcam_feed/', views.webcam_feed, name='webcam_feed'),
#  path('stop-webcam-thread/',views.stop_webcam_thread,name="stop_webcam_thread")
#  path('webcam_feed/', views.webcam_feed, name='webcam_feed'),
#  path('abc', views.WebcamWithIris.as_view(), name='webcam_with_human'),
  
]
