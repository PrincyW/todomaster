from django.contrib import admin
from .models import Category, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'due_date', 'priority', 'completed')
    list_filter = ('completed', 'priority', 'category')
    search_fields = ('title', 'description')

admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
