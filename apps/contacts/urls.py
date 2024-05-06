from django.urls import path
from apps.base.views import contact

urlpatterns = [
    path('contact', contact, name = 'contact')
]
