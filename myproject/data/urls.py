# data/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_data, name='add_data'),
    path('edit/<int:pk>/', views.edit_data, name='edit_data'),
    path('delete/<int:pk>/', views.delete_data, name='delete_data'),
]