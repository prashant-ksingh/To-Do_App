from django.shortcuts import render
from todo.models import Todo, User
from django.shortcuts import redirect,get_object_or_404
import hashlib
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout





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

         password = make_password(user_password)

        #  print(password)

         user_created =User.objects.create(
              name = user_name,
              email = user_email,
              password = password
         )
         print("created user sucessfully")
         if user_created:
               return redirect('success')
        
    else :
         print("NOT calling post")
    
    return render(request, 'signup.html')

def sucess(request):
        return render(request, 'sucessful.html')


# def login(request):
#     if request.method == 'POST':
#         provided_email = request.POST.get('email')
#         provided_password = request.POST.get('password')
        
#         # user_obj = User.objects.all()
#         try:
#             auth_obj = User.objects.get(email = provided_email)
#             print(auth_obj.name)
#             print(auth_obj.email)
#             print(auth_obj.password)

#             is_authenticated = check_password(provided_password, auth_obj.password)

#             # is_authenticated = authenticate(email = provided_email, password = auth_obj.password )


#             if is_authenticated:
#                 print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$User authenticated successfully")
#                 return redirect('show_task')
#             else:
#                 print("Authentication failed")
#         except:
#              print("66666666666666666666666666 No user found")
    
#     return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        provided_email = request.POST.get('email')
        provided_password = request.POST.get('password')
        
        user = authenticate(request, email=provided_email, password=provided_password)

        print("^^^^^^^^^^^^^", user)
        if user is not None:
            auth_login(request, user)  
            print("User authenticated successfully")
            return redirect('show_task')
        else:
            print("Authentication failed")
    
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

     