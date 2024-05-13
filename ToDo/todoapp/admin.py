from .models import Task
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_list = ('task',)

admin.site.register(Task,TaskAdmin)