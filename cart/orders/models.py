from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.
##order model to store the order details about the customer who placed the order it not contains the products details
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((DELETE, 'Delete'), (LIVE, 'Live')) 
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES = ((ORDER_PROCESSED,"ORDER_PROCESSED"), 
                      (ORDER_DELIVERED,"ORDER_DELIVERED"),
                      (ORDER_REJECTED,"ORDER_REJECTED"),
                      )
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.get_order_status_display()} by {self.owner.user.username if self.owner else 'Unknown'}"

class OrderedItem(models.Model):
    product = models.ForeignKey(Product,related_name='added_carts', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
