from django.shortcuts import render, redirect, get_object_or_404
#importa libreria para crear formularios de autenticacion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#libreria para guardar usuarios
from django.contrib.auth.models import User 
#libreria para trabajar dentro de cada usuario
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import RecordForm
from .models import Record
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
    records=Record.objects.filter(user=request.user)

    return render(request,'tasks.html',{'tasks':records})

def create_record(request):

    if request.method == 'GET':
        return render(request, 'create_record.html',{
            'form': RecordForm
        })
    else:
        try:
            #When the method is POST
            form= RecordForm(request.POST)
            new_record=form.save(commit=False)
            new_record.user=request.user
            new_record.save()
            
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_record.html',{
                'form':RecordForm,
                'error': 'Please provide valid data'
            })
            
def record_detail(request,record_id):
    if request.method == 'GET':
        # record=Record.objects.get(pk=record_id) - si no existe el record se cae el servidor por eso es mejor usar el siguiente:
        record=get_object_or_404(Record, pk=record_id,user=request.user)
        form=RecordForm(instance=record)
        return render(request,"record_detail.html",{'record':record, 'form':form})
    else:
        try:
            record=get_object_or_404(Record, pk=record_id,user=request.user)
            form=RecordForm(request.POST, instance=record)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request,"record_detail.html",{'record':record, 'form':form,
            'error':"Error updating record"})
   
        
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

        