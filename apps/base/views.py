from django.shortcuts import render
from apps.base.models import Settings, Title
# Create your views here.

def index(request):
    settings = Settings.objects.all()
    title = Title.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    return render(request, 'base/about,html', locals())

