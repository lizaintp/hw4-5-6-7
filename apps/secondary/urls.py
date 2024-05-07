from django.urls import path
from apps.secondary.views import blog, blog_details, academic, program_single

urlpatterns = [
    path('blog', blog, name = 'blog'),
    path('blog-details', blog_details, name = 'blog-details'),
    path('academic', academic, name = 'academic' ),
    path('program-single', program_single, name = 'program-single')
]
