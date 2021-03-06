from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add-user/', views.add_user, name="add-user"),
    path('add-project/', views.add_project, name="add-project"),
    path('add-task/<project_id>/', views.add_task, name="add-task"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('tender-request/', views.tender_request, name="tender-request"),
    path('request-tender/', views.tender_request, name="request-tender"),
]
