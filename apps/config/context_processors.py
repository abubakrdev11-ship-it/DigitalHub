from .models import Settings

def site_settings(request):
    settings = Settings.objects.first()
    return {'settings': settings}