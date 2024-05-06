from django.shortcuts import render
from apps.contacts.models import Contacts
# Create your views here.

def contact(request):
    contacts = Contacts.objects.all()
    return render(request, "base/contact.html", locals())