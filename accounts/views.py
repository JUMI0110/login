from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    else:
        form = CustomUserCreationForm()


    context = {
        'form': form
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        # request session값을 쿠키에 넣어줘야하기 때문에 넣는 인자
        if form.is_valid():
            # login 함수 불러와서 사용 login(request, 유저정보)
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')
            # next 인자에 url이 있을 때 => 'articles/1/' or 'articles:index'
            # next 인자에 url이 없을 때 => None or 'articles:index' 
            return redirect(next_url or 'articles:index')
    
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

# 쿠키에서 sessionid 삭제
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request, username):
    
    user_profile = User.objects.get(username=username)

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)
