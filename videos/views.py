from django.shortcuts import render, reverse
#from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Videos, Comment, Category
from django.views import View
from .forms import CommentForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class Index(ListView):
    model = Videos
    template_name = 'videos/index.html'
    order_by = '-date_posted'


class CreateVideo(LoginRequiredMixin, CreateView):
    model = Videos
    fields = ['title', 'description', 'video_file', 'thumbnail', 'category']
    template_name = 'videos/create_video.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
# Detail Video Class
class DetailVideo(View):
    def get(self, request, pk, *args, **kwargs):
        video = Videos.objects.get(pk=pk)

        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-created_on')
        categories = Videos.objects.filter(category=video.category)[:15]

        context = {
            'object': video,
            'comments': comments,
            'categories': categories,
            'form': form
        }
        return render(request, 'videos/detail_video.html', context)

    def post(self, request, pk, *args, **kwargs):
        video = Videos.objects.get(pk=pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                user=self.request.user,
                comment=form.cleaned_data['comment'],
                video=video
            )
            comment.save()

        comments = Comment.objects.filter(video=video).order_by('-created_on')
        categories = Videos.objects.filter(category=video.category)[:15]

        context = {
            'object': video,
            'comments': comments,
            'categories': categories,
            'form': form
        }
        return render(request, 'videos/detail_video.html', context)

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
    
# Video Category
class VideoCategoryList(View):
    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        videos = Videos.objects.filter(category=pk).order_by('-date_posted')
        context = {
            'category': category,
            'videos': videos
        }

        return render(request, 'videos/video_category.html', context)
    
# Search Video
class SearchVideo(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        query_list = Videos.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(user__username__icontains=query)
        )

        context = {
            'query_list': query_list,
        }

        return render(request, 'videos/search.html', context)