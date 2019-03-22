from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    type_of_user = models.CharField(max_length=1, choices=[("m", "Manager"), ("c", "Contractor")])

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    under_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
