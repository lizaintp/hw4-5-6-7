from django.shortcuts import render
from apps.contacts.models import Contacts, OtherContacts
# Create your views here.

def contact(request):
    contacts = Contacts.objects.all()
    othercontacs = OtherContacts.objects.all()
    return render(request, "base/contact.html", locals())