from django.shortcuts import render
from apps.base.models import Settings, Title, Student, Graduate, LifelongLearning, LifeinCampus, TuitionFees, Scholarships, AlumniEvent, History, MissionValuesRight, MissionValuesLeft, OurCampusTour, Feedback
# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    title = Title.objects.all()
    student = Student.objects.all()
    graduate = Graduate.objects.all()
    lifelonglearning = LifelongLearning.objects.all()
    lifeincampus = LifeinCampus.objects.all()
    tuitionfees = TuitionFees.objects.all()
    scholarships = Scholarships.objects.all()
    alumnievent = AlumniEvent.objects.all()
    history = History.objects.all()
    mission_values_right = MissionValuesRight.objects.all()
    mission_values_left = MissionValuesLeft.objects.all()
    ourcampustour = OurCampusTour.objects.all()
    feedback = Feedback.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    settings = Settings.objects.latest('id')
    return render(request, 'base/about.html', locals())

