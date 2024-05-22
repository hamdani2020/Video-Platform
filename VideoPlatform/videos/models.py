from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class Videos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='uploads/video_files', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'webm'])])
    thumbnail = models.FileField(upload_to='uploads/thumbnails', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])
    date_posted = models.DateTimeField(default=timezone.now)
