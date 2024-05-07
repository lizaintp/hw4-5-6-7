from django.contrib import admin
from apps.base.models import Settings, Title

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
