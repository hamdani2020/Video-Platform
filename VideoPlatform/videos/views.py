from django.shortcuts import render, reverse
#from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Videos
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, 'videos/index.html') #must include {}

class CreateVideo(LoginRequiredMixin, CreateView):
    model = Videos
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'videos/create_video.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
class DetailVideo(DetailView):
    model = Videos
    template_name = 'videos/detail_video.html'

# Update Video
class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Videos
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.user

    
# Delete Video
class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Videos
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse('index')
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.user