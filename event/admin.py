from django.contrib import admin
from .models import AddEvent, Attending, Category #import models from the current directory

# Register your models here.
"""
allow the creation, update and deletion of the following models, from the admin panel.
"""
admin.site.register(AddEvent)
admin.site.register(Attending)
admin.site.register(Category)