from django.shortcuts import render
from apps.base.models import Settings, Title, Student, Graduate, LifelongLearning, LifeinCampus
# Create your views here.

def index(request):
    settings = Settings.objects.all()
    title = Title.objects.all()
    student = Student.objects.all()
    graduate = Graduate.objects.all()
    lifelonglearning = LifelongLearning.objects.all()
    lifeincampus = LifeinCampus.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    return render(request, 'base/about,html', locals())

