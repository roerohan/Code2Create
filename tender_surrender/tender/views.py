from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import Manager, Contractor, Project, Task, Link
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_user(request, type_of_user):
    if request.method == 'GET':
        return HttpResponseNotFound("<h1>Requested page does not exist</h1>")
    else:
        name = request.POST.get("name");
        password = request.POST.get("password")
        if type_of_user == 'c':
            new_contractor = Contractor(name=name, password=password)
            new_contractor.save()
            return HttpResponse("Added")
        elif type_of_user == 'm':
            new_manager = Manager(name=name, password=password)
            new_manager.save()
            return HttpResponse("Added")
        else:
            return HttpResponseNotFound("<h1>Requested page does not exist</h1>")

@csrf_exempt
def add_project(request):
    if request.method == 'GET':
        return HttpResponseNotFound("<h1>Requested page does not exist</h1>")
    else:
        name = request.POST.get("name");
        description = request.POST.get("description");
        new_project = Project(name=name, description=description)
        new_project.save()
        return HttpResponse("Added")

@csrf_exempt
def add_task(request, project_id):
    if request.method == 'GET':
        return HttpResponseNotFound("<h1>Requested page does not exist</h1>")
    else:
        name = request.POST.get("name");
        description = request.POST.get("description")
        under_project = Project.objects.get(id=project_id)
        new_task = Task(name=name, description=description)
        new_task.under_project = under_project
        new_task.save()
        return HttpResponse("Added")

@csrf_exempt
def tender_request(request):
    manager = Manager.objects.get(id=manager_id)
    contractor = Contractor.objects.get(id=contractor_id)
    task = Task.objects.get(id=task_id)
    link = Link(requested_by='m', status='o')
    link.manager = manager
    link.contractor = contractor
    link.task = task
    link.save()
    # Send notification to contractors

@csrf_exempt
def request_tender(request):
    manager = Manager.objects.get(id=manager_id)
    contractor = Contractor.objects.get(id=contractor_id)
    task = Task.objects.get(id=task_id)
    link = Link(requested_by='c', status='o')
    link.manager = manager
    link.contractor = contractor
    link.task = task
    link.save()
    # Send notification to manager

@csrf_exempt
def close_request(request):
    link_id = request.POST.get("link_id")
    link = Link.objects.get(id="link_id")
    link.status='c'
    link.save()
