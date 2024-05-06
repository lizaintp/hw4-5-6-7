from django.shortcuts import render
from apps.base.models import Settings
# Create your views here.

def index(request):
    settings = Settings.objects.all()
    return render(request, 'base/index.html', locals())

