from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def list_tasks(request):
  tasks = Task.objects.all()
  return render(request, 'list_tasks.html', {"tasks": tasks})

def create_task(request):
  print(request.POST)
  done = False
  
  if request.POST['done']:
    done = True
  else:
    done = False
    
  task = Task(title=request.POST['title'], description=request.POST['description'], done= done)
  task.save()
  return redirect('/tasks/')

def update_task(request, id):
  print(request.POST)
  # print(id)
  task = get_object_or_404(Task, id=id)
  tasks = Task.objects.all()
  
  return render(request,'update_task.html', {"select":task, "tasks": tasks})

def put_task(request, id): 
  print(request.POST['done'])
  done = False
  if done == 'on':
    done = True
  else:
    done == False
    
  Task.objects.filter(id = id).update(title=request.POST['title'], description=request.POST['description'], done= done)
  return redirect('/tasks/')



def delete_task(request, id):
  print(id)
  task = Task.objects.get(id = id)
  task.delete()
  return redirect('/tasks/')