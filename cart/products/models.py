from django.db import models
from customers.models import Customer

# Create your models here.
class Product(models.Model): 
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((DELETE, 'Delete'), (LIVE, 'Live')) ## this product is still live or not
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)
    ##image = models.ImageField(upload_to='media/')
    # New fields for media
    media_file = models.FileField(upload_to='media/', blank=True, null=True)
    media_type = models.CharField(max_length=10, blank=True, null=True) # 'image' or 'video'
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
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