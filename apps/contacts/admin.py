from django.contrib import admin
from apps.contacts.models import Contacts, OtherContacts

# Register your models here.
class ContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('city', )
    list_display = ('city', 'phone')
    search_fields = ('city', 'phone')
admin.site.register(Contacts, ContactsFilterAdmin)

class OtherContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'phone', 'email')
    search_fields = ('city', 'phone', 'email')
admin.site.register(OtherContacts, OtherContactsFilterAdmin)