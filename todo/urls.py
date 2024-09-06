from django.urls import path
from todo import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('sucess/', views.sucess, name='success'),
    path('show_task/', views.show_task, name='show_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
]
