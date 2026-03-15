from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    return render(request, "home.html", {"tasks": tasks})


def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(task=task)
    return redirect('home')