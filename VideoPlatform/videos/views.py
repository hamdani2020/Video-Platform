from django.shortcuts import render, reverse
#from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Videos

def index(request):
    return render(request, 'index.html') #must include {}

class CreateVideo(CreateView):
    model = Videos
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'create_video.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
class DetailVideo(DetailView):
    model = Videos
    template_name = 'detail_video.html'