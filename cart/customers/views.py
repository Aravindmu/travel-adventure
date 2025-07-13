from django.shortcuts import render ,redirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


def signout(request):
    logout(request)
    return redirect('home')


# Create your views here.
def show_account(request):

    context = {}# Initialize context dictionary
    
    if request.POST and 'register' in request.POST:
        context['register'] = True# Show registration form
        username = request.POST.get('username')
        print("Username received:", username)

        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            # Create a new user for registration
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            print("Creating Customer with name:", username)

            # create a profile for the user
            customer = Customer.objects.create(
                user=user,
                name=username,
                address=address,
                phone=phone,
            )
            success_message = "Registration successful! Welcome"
            messages.success(request, success_message)

        ## return redirect('home')
        except Exception as e:
            error_message = "An error occurred during registration: "
            messages.error(request, error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False # Show login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'account.html', context)
