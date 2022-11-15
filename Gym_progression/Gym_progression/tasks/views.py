from django.shortcuts import render, redirect
#importa libreria para crear formularios de autenticacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#libreria para guardar usuarios
from django.contrib.auth.models import User 
#libreria para trabajar dentro de cada usuario
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            #register user
            try:
                user= User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect(tasks)
            except IntegrityError:
                return render(request, 'signup.html',{
                'form':UserCreationForm,
                'error': 'Username already exist'
                })

        else:

           return render(request, 'signup.html',{
                'form':UserCreationForm,
                'error': "Password do not match"
                })

def tasks(request):
    return render(request,'tasks.html')
#no se pone logout porq como se importó la libreria login, es un comando q ocasiona conflicto
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':

        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user= authenticate(
            request, username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'username or password is incorrect'
            })
        else: 
            login(request,user)
            return redirect('tasks')

        