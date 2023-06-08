from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from .models import Todo
from datetime import datetime
from django.contrib import auth
# Create your views here.

def say_hello(request):
    all_todo = Todo.objects.all()
    alltodo={
        'alltodo':all_todo
        }
    return render(request,'index.html',alltodo)

def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo = Todo(title=title, desc=desc, date_created=datetime.today())
        todo.save()
    all_todo = Todo.objects.all()
    alltodo={
        'alltodo':all_todo
        }
    return render(request,'index.html',alltodo)


def about(request):
    variable ={
        'text':'This is about page'
    }
    return render(request, 'about.html', variable)
    #return HttpResponse("this is about")

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user1 = Users(email=email,username=username,password=password)
        user1.save()

    return render(request, 'Signup.html')

def users(request):
    users=Users.objects.all()
    all_users={
        'all_users':users
    }
    return render(request,'users.html',all_users)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        a=Users.objects.all().filter(username=username, password= password)
        print(a)
        if a:
            #session['email'] = username
            return render(request,"index.html")
        else:
            msg = "Invalid username or password"
            return render(request,'login.html', msg)

    return render(request,'login.html')

def delete(request,sno):
    todo = Todo.objects.get(sno=sno)
    print(todo)
    todo.delete()
    return index(request)

def update(request,sno):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        todo = Todo.objects.get(sno=sno)
        todo.title = title
        todo.desc = desc
        todo.save()
        return say_hello(request)

    alltodo = Todo.objects.get(sno=sno)
    todo={
        'todo':alltodo
    }
    return render(request,'update.html', todo)