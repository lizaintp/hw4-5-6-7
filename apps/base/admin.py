from django.contrib import admin
from apps.base import models

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('fullname', )
    list_display = ('fullname',)
    search_fields = ('fullname',)
admin.site.register(models.Settings, SettingsFilterAdmin)

class TitleFilterAdmin(admin.ModelAdmin):
    list_filter = ('desc', )
    search_fields = ('desc', 'subdesc')
admin.site.register(models.Title, TitleFilterAdmin)

class StudentFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(models.Student, StudentFilterAdmin)

class GraduateFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(models.Graduate, GraduateFilterAdmin)

class LifelongLearningFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(models.LifelongLearning, LifelongLearningFilterAdmin)

class LifeinCampusFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(models.LifeinCampus, LifeinCampusFilterAdmin)

class TuitionFeesFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(models.TuitionFees, TuitionFeesFilterAdmin)

admin.site.register(models.Scholarships)

class AlumniEventFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'time', 'data', 'location')
    search_fields = ('title','time', 'data', 'location')
admin.site.register(models.AlumniEvent, AlumniEventFilterAdmin)

class HistoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'desc')
    search_fields = ('title', 'desc')
admin.site.register(models.History, HistoryFilterAdmin)

class MissionValuesRightFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
admin.site.register(models.MissionValuesRight, MissionValuesRightFilterAdmin)

class OurCampusTourFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
admin.site.register(models.OurCampusTour, OurCampusTourFilterAdmin)

class FeedbackFilterAdmin(admin.ModelAdmin):
    list_filter = ('autor', )
    list_display = ('autor','profession')
    search_fields = ('autor', 'profession')
admin.site.register(models.Feedback, FeedbackFilterAdmin)

