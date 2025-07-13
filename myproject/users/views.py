# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from data.models import UserData


@login_required
def home(request):
    # Fetch all UserData entries
    all_user_data_entries = UserData.objects.all().order_by('-created_at') # Order by latest
    context = {
        'user': request.user,#current user
        'all_user_data_entries': all_user_data_entries # Renamed for clarity
    }
    return render(request, 'users/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()##first save and next passed through login
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()## show the blank form
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()#fetch the current user for login process
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login') # Or wherever you want to redirect after logout

@login_required
def home(request):
    user_data_entries = UserData.objects.filter(user=request.user) #filter the currently logged user only
    context = {
        'user': request.user,
        'user_data_entries': user_data_entries #The result is a QuerySet containing just that user's data
    }
    return render(request, 'users/home.html', context)