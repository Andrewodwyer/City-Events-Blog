from django.contrib import admin
from .models import AddEvent

# Register your models here.
"""
allow the creation, update and deletion of event AddEvent from the admin panel.
"""
admin.site.register(AddEvent)
