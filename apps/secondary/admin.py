from django.contrib import admin
from apps.secondary.models import Blog

# Register your models here.
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('autor', )
    list_display = ('autor', 'date')
    search_fields = ('autor', 'date', 'title')
admin.site.register(Blog, BlogFilterAdmin)