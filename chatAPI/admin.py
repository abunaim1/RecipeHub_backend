from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name', 'verified']



admin.site.register(Profile, ProfileAdmin)
