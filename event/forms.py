from django import forms
from .models import AddEvent

class AddEventForm(forms.ModelForm):
    class Meta:
        """
        Meta data give information to the form, Which model it is and a list of fields
        that will be in the form.
        The widgets dictionary allows overriding the default Django behavior by specifying
        exactly how the fields are to be rendered in the form.
        attrs parameter allows me to specify the HTML attributes
        type': 'datetime-local is more user friendly and allow for both date and time in the 1 field
        """
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