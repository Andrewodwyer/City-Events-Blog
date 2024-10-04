from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import AddEvent, Attending, Category, Comment
# import models from the current directory


@admin.register(AddEvent)
class AddEventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'updated_on')
    # controls which fields to display on admin dashboard.
    search_fields = ['title', 'description']
    # Limits the fields to search
    list_filter = ('status', 'updated_on',)
    # Filter on right showing the status, draft or published
    prepopulated_fields = {'slug': ('title',)}
    # The slug will be prepopulated by the title text
    summernote_fields = ('description',)
    # summernote_field, user can format the content, bold underline, font etc


# Register your models here.
"""
allow the creation, update and deletion of the following models
from the admin panel.
"""

admin.site.register(Attending)
admin.site.register(Category)
admin.site.register(Comment)
