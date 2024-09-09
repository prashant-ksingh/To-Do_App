from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import redirect,get_object_or_404
import hashlib
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User





def home(request):
        return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
         print("call in post")
         user_name = request.POST.get('user_name')
         user_email = request.POST.get('user_email')
         user_password = request.POST.get('user_password')

        #  md5_hash = hashlib.md5()
        #  md5_hash.update(user_password.encode('utf-8'))
        #  password = md5_hash.hexdigest()

         user = User.objects.filter(username = user_name)
         if user:
          messages.info(request, 'Username already taken')
          return redirect('signup')

         user_created =User.objects.create(
              username = user_name,
              email = user_email,
         )

         user_created.set_password(user_password)
         user_created.save()

         print("created user sucessfully")
         if user_created:
               return redirect('success')
        
    else :
         print("NOT calling post")
    
    return render(request, 'signup.html')

def sucess(request):
        return render(request, 'sucessful.html')


def login(request):
    if request.method == "POST":
         username = request.POST.get('user_name')
         password = request.POST.get('password')

         print("$$$$$$$$$$$", username, password)
    return render(request, 'login.html')



def logout(request):
    return render(request, '')

@login_required()
def show_task(request):
    all_task = Todo.objects.all()
    return render(request, 'addtask.html', {
        "all_task": all_task
    })

def add_task(request):
    if request.method == 'POST':
 
        task_name = request.POST.get('name')
        task_desc = request.POST.get('desc')
        
        Todo.objects.create(
            taskname=task_name,
            description=task_desc
        )
        
        return redirect('show_task')


def delete_task(request, id):
    task = get_object_or_404(Todo, id=id)
    task.delete()
    return redirect('show_task')

     