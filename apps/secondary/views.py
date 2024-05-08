from django.shortcuts import render
from apps.secondary.models import Blog, FacultyDirectory, Info, Event, Alumni
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", locals())

def blog_details(request):
    return render(request, 'blog-details.html', locals())

def academic(request):
    return render(request, 'academic.html', locals())

def admission(request):
    return render(request, 'admission.html', locals())

def alumni(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni.html', locals())

def athletics(request):
    return render(request, 'athletics.html', locals())

def campus_life(request):
    return render(request, 'campus-life.html', locals())

def event_details(request):
    return render(request, 'event-details.html', locals())

def event(request):
    event = Event.objects.all()
    return render(request, 'event.html', locals())

def faculty(request):
    facultydirectory = FacultyDirectory.objects.all()
    return render(request, 'faculty.html', locals())

def faculty_details(request, id):
    info = Info.objects.all()
    info_detail = Info.objects.get(id=id)
    return render(request, 'faculty-details.html', locals())

def notice_details(request):
    return render(request, 'notice-details.html', locals())

def research(request):
    return render(request, 'research.html', locals())

def scholarship(request):
    return render(request, 'scholarship.html', locals())

def tution_fee(request):
    return render(request, 'tution-fee.html', locals())