from django.contrib import admin
from .models import User, Project, Task


admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
