from django.shortcuts import render
from todo import forms
from django.views.decorators.csrf import csrf_exempt

def home(request):
    #  if request.method == 'POST':

    #     if(request.name == 'login'):
    #        return render(request, 'login.html')
        
    #     if(request.name == 'signup'):
    #        return render(request, 'signup.html') 
    #  else: 
        return render(request, 'home.html')
@csrf_exempt
def add_task(request):
    print("add task called")
    print(request.POST)
    return render(request, 'addtask.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, '')

def signup(request):
    return render(request, 'signup.html')

def test(request):
    return render(request, 'addtask.html')