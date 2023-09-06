from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    errorLength = True
    print("obteniendo datos", request.POST)
    if request.method == "GET":
        print("enviando formulario")
        return render(
            request, "signup.html", {"form": UserCreationForm, "error": False}
        )
    elif request.method == "POST":
        if request.POST["password"] != request.POST["repassword"]:
            return render(
                request, "signup.html", {"form": UserCreationForm, "errorRe": True}
            )

        if len(request.POST["password"]) < 8:
            return render(
                request, "signup.html", {"form": UserCreationForm, "error": errorLength}
            )

        errorLength = False

        try:
            # Register User
            user = User.objects.create_user(
                request.POST["email"], request.POST["email"], request.POST["password"]
            )
            user.save()
            return render(
                request, "signup.html", {"form": UserCreationForm, "error": errorLength}
            )
        except:
            print("error")


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})


def create_task(request):
    done = False

    try:
        if request.POST["done"]:
            done = True
        else:
            done = False
    except:
        done = False

    task = Task(
        title=request.POST["title"], description=request.POST["description"], done=done
    )
    task.save()
    return redirect("/main/")


def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()

    return render(request, "update_task.html", {"select": task, "tasks": tasks})


def put_task(request, id):
    done = False
    try:
        if request.POST["done"]:
            done = True
        else:
            done == False
    except:
        done = False

    Task.objects.filter(id=id).update(
        title=request.POST["title"], description=request.POST["description"], done=done
    )
    return redirect("/main/")


def delete_task(request, id):
    print(id)
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/main/")
