from django.contrib import admin
from django.urls import path
from .views import CreateVideo, DetailVideo

urlpatterns = [
    path('create/', CreateVideo.as_view(), name='create-video'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
]