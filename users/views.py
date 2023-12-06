from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


def signup(request):
    
    if request.method == "GET": #화면 띄우기 용도
        return render(request, 'webpage.html')
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
            
        return redirect('login')
    
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


    




