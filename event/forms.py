from django import forms
from .models import AddEvent

class AddEventForm(forms.ModelForm):
    class Meta:
        model = AddEvent
        fields = [
            'title', 'slug', 'description', 'event_category', 'start_date_time',
            'end_date_time', 'location', 'is_free', 'price', 'link_to_event_page', 
            'excerpt', 'event_image'
        ]
        widgets = {
            'start_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }