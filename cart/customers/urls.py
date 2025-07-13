from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('account',views.show_account, name='account'), 
    path('signout', views.signout, name='signout'),
]