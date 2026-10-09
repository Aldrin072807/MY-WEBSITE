from django.contrib import admin
from .models import ContactMessage, Project

admin.site.register(Project)
admin.site.register(ContactMessage)