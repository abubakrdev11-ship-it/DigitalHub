from django.shortcuts import render
from apps.config.models import Settings, Services

# Create your views here.
def index(request):
    settings = Settings.objects.first()
    services = Services.objects.all()
    return render(request, 'index.html', locals())

def contacts(request):
    return render(request, 'contacts.html', locals())

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', locals())

def about(request):
    return render(request, 'about.html', locals())