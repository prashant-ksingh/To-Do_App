from django.shortcuts import render
from todo import models

def home(request):
    return render(request, 'home.html')

def task(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, '')

def signup(request):
    return render(request, 'signup.html')