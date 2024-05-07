from django.urls import path
from apps.base.views import index, about

urlpatterns = [
    path('', index, name = 'index'),
    path('', about, name = 'about')
]
