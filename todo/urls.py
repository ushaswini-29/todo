from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.addTask, name='addTask'),
    path('complete-task/<int:id>/', views.completeTask, name='completeTask'),
    path('delete-task/<int:id>/', views.deleteTask, name='deleteTask'),
]