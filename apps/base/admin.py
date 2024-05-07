from django.contrib import admin
from apps.base.models import Settings, Title, Student, Graduate, LifelongLearning, LifeinCampus

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('fullname', )
    list_display = ('fullname',)
    search_fields = ('fullname',)
admin.site.register(Settings, SettingsFilterAdmin)

class TitleFilterAdmin(admin.ModelAdmin):
    list_filter = ('desc', )
    search_fields = ('desc', 'subdesc')
admin.site.register(Title, TitleFilterAdmin)

class StudentFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Student, StudentFilterAdmin)

class GraduateFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Graduate, GraduateFilterAdmin)

class LifelongLearningFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(LifelongLearning, LifelongLearningFilterAdmin)

class LifeinCampusFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(LifeinCampus, LifeinCampusFilterAdmin)