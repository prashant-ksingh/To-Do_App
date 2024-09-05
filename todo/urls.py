from django.urls import path
from todo import views


urlpatterns = [
    path('',views.home),
    path('add_task',views.add_task),
    path('login',views.login),
    path('logout',views.logout),
    path('signup',views.signup),
    path('test',views.test),
]
