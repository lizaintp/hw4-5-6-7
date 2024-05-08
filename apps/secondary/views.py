from django.shortcuts import render
from apps.secondary.models import Blog, FacultyDirectory, Info, Event, Alumni, CampusLive, StudentLife, ArtCulture, Sport, Academics, Purpose, UpcomingEvent
from apps.base.models import Settings, Feedback
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    settings = Settings.objects.latest('id')
    return render(request, "blog.html", locals())

def blog_details(request):
    settings = Settings.objects.latest('id')
    return render(request, 'blog-details.html', locals())

def academic(request):
    settings = Settings.objects.latest('id')
    feedback = Feedback.objects.all()
    academics = Academics.objects.all()
    purpose = Purpose.objects.all()

    return render(request, 'academic.html', locals())

def admission(request):
    settings = Settings.objects.latest('id')
    return render(request, 'admission.html', locals())

def alumni(request):
    settings = Settings.objects.latest('id')
    upcomingevent = UpcomingEvent.objects.all()
    alumni = Alumni.objects.all()
    return render(request, 'alumni.html', locals())

def athletics(request):
    settings = Settings.objects.latest('id')
    return render(request, 'athletics.html', locals())

def campus_life(request):
    settings = Settings.objects.latest('id')
    campus_life = CampusLive.objects.all()
    art_culture = ArtCulture.objects.all()
    sport = Sport.objects.all()
    return render(request, 'campus-life.html', locals())

def event_details(request):
    settings = Settings.objects.latest('id')
    return render(request, 'event-details.html', locals())

def event(request):
    settings = Settings.objects.latest('id')
    event = Event.objects.all()
    return render(request, 'event.html', locals())

def faculty(request):
    settings = Settings.objects.latest('id')
    facultydirectory = FacultyDirectory.objects.all()
    student_life = StudentLife.objects.all()
    return render(request, 'faculty.html', locals())

def faculty_details(request, id):
    settings = Settings.objects.latest('id')
    info = Info.objects.get(id=id)
    latest_info = Info.objects.latest('id')
    return render(request, 'faculty-details.html', locals())

def faculty_detailss(request):
    settings = Settings.objects.latest('id')
    info = Info.objects.all()
    return render(request, 'faculty-details.html', locals())

def notice_details(request):
    settings = Settings.objects.latest('id')
    return render(request, 'notice-details.html', locals())

def research(request):
    settings = Settings.objects.latest('id')
    return render(request, 'research.html', locals())

def scholarship(request):
    settings = Settings.objects.latest('id')
    return render(request, 'scholarship.html', locals())

def tution_fee(request):
    settings = Settings.objects.latest('id')
    return render(request, 'tution-fee.html', locals())