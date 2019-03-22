from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import User, Project, Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_user(request, type_of_user):
    if request.method == 'GET':
        return HttpResponseNotFound("<h1>Requested page does not exist</h1>");
    else:
        name = request.POST.get("name");
        password = request.POST.get("password");
        new_user = User(name=name, password=password, type_of_user=type_of_user)
        new_user.save()
        return HttpResponse("Added")

@csrf_exempt
def add_project(request):
    if request.method == 'GET':
        return HttpResponseNotFound("<h1>Requested page does not exist</h1>");
    else:
        name = request.POST.get("name");
        description = request.POST.get("description");
        new_project = Project(name=name, description=description)
        new_project.save()
        return HttpResponse("Added")

@csrf_exempt
def add_task(request, project_id):
    if request.method == 'GET':
        return HttpResponseNotFound("<h1>Requested page does not exist</h1>");
    else:
        name = request.POST.get("name");
        description = request.POST.get("description")
        under_project = Project.objects.get(id=project_id)
        new_task = Task(name=name, description=description)
        new_task.under_project = under_project
        new_task.save()
        return HttpResponse("Added")

# @csrf_exempt
# def tender_request(request):
