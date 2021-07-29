import registerapp
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


@login_required(login_url='login')
def homePage(request):
    return render(request, 'registerapp/home.html')


def register(request):
    form = RegisterForm
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    

    context = {'form':form}
    return render(request, 'registerapp/registerpage.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    context = {}
    return render(request, 'registerapp/loginpage.html', context)
