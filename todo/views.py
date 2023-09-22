from django.shortcuts import render
from todo import forms

def home(request):
     if request.method == 'POST':

        if(request.name == 'login'):
           return render(request, 'login.html')
        
        if(request.name == 'signup'):
           return render(request, 'signup.html') 
        
     else: 
        return render(request, 'home.html')

def task(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, '')

def signup(request):
    return render(request, 'signup.html')