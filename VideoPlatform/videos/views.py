from django.shortcuts import render, reverse
#from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Videos
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'index.html') #must include {}

class CreateVideo(LoginRequiredMixin, CreateView):
    model = Videos
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'create_video.html'

    # Forms
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
class DetailVideo(DetailView):
    model = Videos
    template_name = 'detail_video.html'

# Update Video
class UpdateVideo(LoginRequiredMixin, UpdateView):
    model = Videos
    fields = ['title', 'description']
    template_name = 'create_video.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
# Delete Video
class DeleteVideo(LoginRequiredMixin, DeleteView):
    model = Videos
    template_name = 'delete_video.html'

    def get_success_url(self):
        return reverse('index')