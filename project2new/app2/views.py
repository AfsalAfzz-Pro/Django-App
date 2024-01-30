from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def HomePage(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin')
        else:
            return render(request, 'home.html')
    return redirect('login')

@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def SignupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("The passwords are not the same")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request, 'signup.html')



@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username = username, password = password)
        print(user)
        # if user.is_superuser:
        #     print('superuser is in')
        #     return redirect('Admin') 
        if user is not None:
            print(' you are correct ')
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid credentials')
    return render(request, 'index.html')




@login_required(login_url = 'login')
def LogoutPage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')




