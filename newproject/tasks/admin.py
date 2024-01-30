from django.contrib import admin
from tasks.models import Task

# Register your models here.
@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    fields = ('title', 'description')