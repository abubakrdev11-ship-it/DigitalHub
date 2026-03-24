from django.urls import path
from .views import index, contacts, services, about

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
]