from django.contrib import admin
from htmx_samples_app.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass