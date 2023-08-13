from django.shortcuts import render,redirect
from task.forms import TaskModalForm
from task.models import TaskModel

def home(request):
    return render(request,'home.html')

def addItem(request):
    if request.method == 'POST':
        task_form = TaskModalForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            print(task_form.cleaned_data)
            return redirect('allItem')
    else:
        task_form = TaskModalForm()

    return render(request, 'addItem.html', {'form': task_form})

def allItem(request):
    task = TaskModel.objects.all()
    print(task)
    return render(request,'AllItem.html',{'data':task})


def completeTasks(request):
    complete = TaskModel.objects.all()
    print(complete)
    return render(request,'completeTask.html',{'data':complete})

def editTask(request,id):
    task = TaskModel.objects.get(pk = id)
    form = TaskModalForm(instance = task)
    if request.method == 'POST':
        form = TaskModalForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('allItem')
    return render(request,'addItem.html',{'form':form})


    

def DelateTask(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('allItem')

def completeDeleteTask(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('complete_tasks')


def CompleteTaskUpdate(request, id):
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    return redirect('complete_tasks')

def DelateCompletedTask(request,id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('complete_tasks')

def complete_editTask(request,id):
    task = TaskModel.objects.get(pk = id)
    form = TaskModalForm(instance = task)
    if request.method == 'POST':
        form = TaskModalForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('complete_tasks')
    return render(request,'addItem.html',{'form':form})
