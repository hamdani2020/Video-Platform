# Generated by Django 5.0.6 on 2024-05-19 22:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_videos_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_file',
            field=models.FileField(upload_to='uploads/video_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]