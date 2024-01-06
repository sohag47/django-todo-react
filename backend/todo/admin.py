from django.contrib import admin

# Register your models here.
from .models import Todo, Organization, Project, Task, Group


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'description', 'status')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'description', 'status')
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'description', 'status')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'description', 'completed')
      

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Todo, TodoAdmin)