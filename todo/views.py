from django.shortcuts import render
from todo.models import Todo
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User





def home(request):
        return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
         print("call in post")
         user_name = request.POST.get('user_name')
         user_email = request.POST.get('user_email')
         user_password = request.POST.get('user_password')

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

        #  print("$$$$$$$$$$$", username, password)

         if not User.objects.filter( username = username).exists():
              messages.error(request, 'Invalid username')
              return redirect('login')
         
         user = authenticate(username = username, password = password)
         if user is None:
              messages.error(request, 'Invalid password')
              return redirect('login')
         else:
              auth_login(request, user)
              return redirect('show_task')
         
         
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required()
def show_task(request):
    user = request.user
    tasks = Todo.objects.filter(id=user.id)

    return render(request, 'addtask.html', {
        "all_task": tasks
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

     