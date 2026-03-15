from django.shortcuts import render, redirect
from .models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }

    return render(request, 'home.html', context)


def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(task=task)

    return redirect('home')


def completeTask(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()

    return redirect('home')


def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('home')