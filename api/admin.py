from django.contrib import admin
from .models import Project, Place


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['project', 'id', 'is_visited', 'created_at']
    list_filter = ['is_visited', 'created_at']
    search_fields = ['id', 'notes']