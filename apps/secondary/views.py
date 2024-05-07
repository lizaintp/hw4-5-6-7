from django.shortcuts import render
from apps.secondary.models import Blog
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", locals())

def blog_details(request):
    return render(request, 'blog-details.html', locals())

def academic(request):
    return render(request, 'academic.html', locals())

def program_single(request):
    return render(request, 'program-single.html', locals())
