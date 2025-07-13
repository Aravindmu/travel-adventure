# data/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserData
from .forms import UserDataForm

@login_required
def add_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES) # Pass request.FILES for file uploads
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.user = request.user
            user_data.save()
            return redirect('home')
    else:
        form = UserDataForm()
    return render(request, 'data/add_edit_data.html', {'form': form})

@login_required
def edit_data(request, pk):
    user_data = get_object_or_404(UserData, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES, instance=user_data) # Pass request.FILES
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserDataForm(instance=user_data)
    return render(request, 'data/add_edit_data.html', {'form': form})

@login_required
def delete_data(request, pk):
    user_data = get_object_or_404(UserData, pk=pk, user=request.user)
    if request.method == 'POST':
        # Optional: Delete the file from storage when deleting the record
        if user_data.media_file:
            user_data.media_file.delete(save=False) # save=False prevents a database save
        user_data.delete()
        return redirect('home')
    return render(request, 'data/confirm_delete.html', {'user_data': user_data})