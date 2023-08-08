from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import cache_control

# Create your views here.

# Log in page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if request.user.is_authenticated:
        messages.warning(request,'If you needs to go to login page click "log out"')
        return redirect('/home')
    if request.method=="POST":
        user1=request.POST['name']
        pass1=request.POST['password']
        print(user1,pass1,"hello")
        if user1=='' and pass1=="":
            messages.warning(request,'Enter your username and password')
            return redirect('/')
        if user1=='':
            messages.warning(request,'Enter your username')
            return redirect('/')
        myUser=authenticate(username=user1,password=pass1)
        
        if myUser is not None:
            messages.success(request,'successfully signed in')
            login(request,myUser)
            return redirect('home/')
        else:
            messages.warning(request,'password is wrong')
            return redirect('/')

    return render(request,'UserPartition/index.html')

# Sign up page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.user.is_authenticated:
        messages.success(request,'If you needs to go to login page click "log out"')
        return redirect('/home')
    if request.method=="POST":
        name=request.POST.get('name')
        email1=request.POST.get('email')
        password1=request.POST.get('password')
        if name=="" and email1=="" and password1=="":
            messages.warning(request,'Enter those forms')
            return redirect('/reg')
        if name=="":
            messages.warning(request,'Enter your name ')
            return redirect('/reg')
        if email1=="":
            messages.warning(request,'Enter your email')
            return redirect('/reg')
        if password1=="":
            messages.warning(request,'Enter your password')
            return redirect('/reg')
        try:
            if User.objects.get(username=name):
                messages.warning(request,'This name already exist')
                return redirect('/reg')
        except:
            pass
        try:
            if User.objects.get(email=email1):
                messages.warning(request,'This email is already taken')
                return redirect('/reg')
        except:
            pass
        
        myUser=User.objects.create_user(name,email1,password1)
        myUser.save()
        return redirect('/')
    return render(request,'UserPartition/register.html')


def home(request):
    if authenticate_page(request):
        print("Hello it is authenticated")
        return render(request,'UserPartition/home.html')
    else:
        return redirect('/')

def price(request):
    if authenticate_page(request):
        return render(request,'UserPartition/price.html')
    else:
        return redirect('/')

def feature(request):
    if authenticate_page(request):
        return render(request,'UserPartition/feature.html')
    else:
        return redirect('/')

def authenticate_page(request):
    if request.user.is_authenticated:
        return True
    else:
        messages.warning(request,'Be sure that you authenticated before entering')
        return False
    
def signout(request):
    logout(request)
    return redirect('/')


# * Admin page

def adminPage(request):
    return render(request,'adminPartition/Index.html')

def adminHome(request):
    return render(request,'adminPartition/home.html')