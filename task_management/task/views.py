from django.shortcuts import render, redirect,get_object_or_404
from .forms import TaskModelForm
from .models import TaskModel
def add_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskModelForm()
    return render(request, 'add_task.html', {'form': form})

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    form = TaskModelForm( instance=task)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect('show_tasks')
