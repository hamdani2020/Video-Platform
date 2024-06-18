from django.contrib import admin
from django.urls import path
from . import views
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo, VideoCategoryList, SearchVideo

urlpatterns = [
    path('create/', CreateVideo.as_view(), name='video-create'),
    #path('create/', CreateVideo.as_view(), name='create-video'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='update-video'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='delete-video'),
    path('category/<int:pk>', VideoCategoryList.as_view(), name='category-list'),
    path('search/', SearchVideo.as_view(), name='video-search'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail')
]