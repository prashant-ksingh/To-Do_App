from django.urls import path
from todo import views


urlpatterns = [
    path('',views.home),
    path('task',views.task),
    path('login',views.login),
    path('logout',views.logout),
    path('signup',views.signup),
]
