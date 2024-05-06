from django.shortcuts import render
from apps.secondary.models import Blog
# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", locals())

def blog_details(request):
    return render(request, 'blog-details.html', locals())