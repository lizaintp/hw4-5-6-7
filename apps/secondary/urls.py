from django.urls import path
from apps.secondary.views import blog, blog_details, academic, admission, alumni, athletics, campus_life, event_details, event, faculty_details, faculty, notice_details,research, scholarship , tution_fee

urlpatterns = [
    path('blog/', blog, name = 'blog'),
    path('blog-details/', blog_details, name = 'blog-details'),
    path('academic/', academic, name = 'academic' ),
    path('admission/', admission, name = 'admission' ),
    path('alumni/', alumni, name = 'alumni' ),
    path('athletics/', athletics, name = 'athletics' ),
    path('campus-life/', campus_life, name = 'campus-life' ),
    path('event-details/', event_details, name = 'event-details' ),
    path('event/', event, name = 'event' ),
    path('faculty-details/<int:id>/', faculty_details, name='faculty-details' ),
    path('faculty/', faculty, name = 'faculty' ),
    path('notice-details/', notice_details, name = 'notice-details' ),
    path('research/', research, name = 'research' ),
    path('scholarship/', scholarship, name = 'scholarship' ),
    path('tution-fee/', tution_fee, name = 'tution-fee' )
]
