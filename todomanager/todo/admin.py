from django.contrib import admin
from todo.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'due_date',
        'completed',
        'created_at'
    )

admin.site.register(Task, TaskAdmin)