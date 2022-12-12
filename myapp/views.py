from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from .forms import CreateNewProject
from .models import Project

# Create your views here.
def home(request):
    return render(request , 'home.html')

def signup(request):

    if request.method == 'GET':
        return render (request , 'signup.html',{'form': UserCreationForm
        })
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("tasks")
                #return HttpResponse('Usuario creado satisfactoriamente')
            except:
                return render (request , 'signup.html',{'form': UserCreationForm ,
                'error':'Usuario ya existente'})
                #return HttpResponse('Usuario ya existente')
        return render (request , 'signup.html',{'form': UserCreationForm ,
                'error':'Contraseña no coincide'})
        #return HttpResponse('Contraseña no coincide')

def tasks(request):
    return render(request , 'tasks.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method== 'GET':
        return render(request,'signin.html' ,{
        'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.html' ,{
                'form':AuthenticationForm,
                'error':'Usuario o contarseña es incorrecto'
                })
        else:
            login(request, user)
            return redirect('tasks')

    # return render(request,'signin.html' ,{
    #     'form':AuthenticationForm
    #     })

    
def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html" ,{
        "projects":projects
    })


def create_project(request):
    if request.method== 'GET':
        return render(request,"create_project.html",{
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(title=request.POST['title'], description=request.POST['description'],foto=request.FILES['foto'], tag=request.POST['tag'], url_git=request.POST['url_git'] )
        return redirect('projects')