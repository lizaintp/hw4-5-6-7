from django.contrib import admin
from apps.secondary import models

# Register your models here.
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('autor', )
    list_display = ('autor', 'date')
    search_fields = ('autor', 'date', 'title')
admin.site.register(models.Blog, BlogFilterAdmin)

class FacultyDirectoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'profession', 'email', 'phone')
    search_fields = ('name', 'profession', 'email', 'phone')
admin.site.register(models.FacultyDirectory, FacultyDirectoryFilterAdmin)

class InfoFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'profession', 'email', 'phone')
    search_fields = ('name', 'profession', 'email', 'phone')
admin.site.register(models.Info, InfoFilterAdmin)

class EventFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'time', 'data', 'location')
    search_fields = ('title','time', 'data', 'location')
admin.site.register(models.Event, EventFilterAdmin)

class AlumniFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(models.Alumni, AlumniFilterAdmin)