from django.contrib import admin
from .models import Settings, Services

# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')
    search_fields = ('title', 'phone', 'email')
    list_filter = ('title', 'phone', 'email')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title', 'price')
    list_filter = ('title', 'price')