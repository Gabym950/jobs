from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'external_id', 'status', 'salary', 'country')
    list_filter = ('status', 'country')
    search_fields = ('title', 'external_id')
    ordering = ('-id',)