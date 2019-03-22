from django.urls import path
from . import views

urlpatterns = [
    path('add-user/<type_of_user>/', views.add_user, name="add-user"),
    path('add-project/', views.add_project, name="add-project"),
    path('add-task/<project_id>/', views.add_task, name="add-task"),
]
