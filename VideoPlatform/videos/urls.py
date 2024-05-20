from django.contrib import admin
from django.urls import path
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo

urlpatterns = [
    path('create/', CreateVideo.as_view(), name='create-video'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='update-video'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='delete-video'),
]