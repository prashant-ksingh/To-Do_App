from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from todo.models import Todo
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect



def home(request):
        return render(request, 'home.html')



def add_task(request):
    if request.method == 'POST':
 
        task_name = request.POST.get('name')
        task_desc = request.POST.get('desc')
        
        Todo.objects.create(
            taskname=task_name,
            description=task_desc
        )
        
        return redirect('show_task')


def show_task(request):
    all_task = Todo.objects.all()
    return render(request, 'addtask.html', {
        "all_task": all_task
    })

def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, '')

def signup(request):
    return render(request, 'signup.html')



def delete_task(request, id):
    task = get_object_or_404(Todo, id=id)
    task.delete()
    return redirect('show_task')

     