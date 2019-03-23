from django.contrib import admin
from .models import Manager, Contractor, Project, Task, Link


admin.site.register(Manager)
admin.site.register(Contractor)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Link)
