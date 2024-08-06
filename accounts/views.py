from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')

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
            return redirect('accounts:login')
    
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)