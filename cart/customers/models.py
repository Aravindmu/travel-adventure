from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model): 
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((DELETE, 'Delete'), (LIVE, 'Live'))##customer is still live in any product or not
    # DELETE_CHOICES = ((DELETE, 'Delete'), (LIVE, 'Live'))  # This line is incorrect; it should be defined before use.
    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile') ## One-to-one relationship with User model for customer profile
    phone = models.CharField(max_length=10)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
