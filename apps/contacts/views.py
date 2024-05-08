from django.shortcuts import render
from apps.base.models import Settings
from apps.contacts.models import Contacts, OtherContacts
# Create your views here.

def contact(request):
    contacts = Contacts.objects.all()
    settings = Settings.objects.latest('id')
    othercontacs = OtherContacts.objects.all()
    return render(request, "base/contact.html", locals())