from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    # TODO add redirect to homepage and logout
    return render(request, 'accounts/signup.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                context = {
                    'error': 'Username has already been taken.'
                }
                return render(request, 'accounts/signup.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=[request.POST['password']])
                auth.login(request, user)
                return redirect('home')

        else:
            context = {
                'error': 'Passwords must match.'
            }
            return render(request, 'accounts/signup.html', context)
        # The user wants to sign up
    else:
        return render(request, 'accounts/signup.html')
