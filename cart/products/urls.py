from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('product_list',views.list_products, name='list_products'), 
    path('product_details/ <pk>',views.detail_product, name='detail_product'),
    path('add/', views.add_content, name='add_content'),
]