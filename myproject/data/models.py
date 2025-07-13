# data/models.py
from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username_field = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    # New fields for media
    media_file = models.FileField(upload_to='user_uploads/', blank=True, null=True)
    media_type = models.CharField(max_length=10, blank=True, null=True) # 'image' or 'video'

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"{self.user.username}'s data: {self.username_field}"

    def save(self, *args, **kwargs):
        # Determine media type before saving
        if self.media_file:
            mimetype = self.media_file.file.content_type
            if mimetype.startswith('image/'):
                self.media_type = 'image'
            elif mimetype.startswith('video/'):
                self.media_type = 'video'
            else:
                self.media_type = None # Or handle other file types
        else:
            self.media_type = None
        super().save(*args, **kwargs)