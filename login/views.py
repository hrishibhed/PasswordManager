from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as logn,logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignUpForm,LoginForm
ADMIN_USERS = 'admin'


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    frm=LoginForm
    error_message=None
    if request.POST:
        frm=LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            if user.username in ADMIN_USERS:
                logn(request, user)
                return redirect('view')
            else:
                logn(request, user)
                return redirect('dashboard')
        else:
            frm=LoginForm()
            error_message='Invalid'

    return render(request,'login.html',{'frm':frm})

    
@login_required
def logout(request):
    auth_logout(request)
    return redirect("login")

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('view')
    if request.method == 'POST':
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('login')
    else:
        frm = SignUpForm()
    return render(request, 'signup.html', {'frm': frm})