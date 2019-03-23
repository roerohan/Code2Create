from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Contractor(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    under_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

class Link(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    requested_by = models.CharField(max_length=1, choices=[("m", "manager"), ("c", "contractor")])
    status = models.CharField(max_length=1, choices=[("o", "open"), ("c", "closed")], null=True)
