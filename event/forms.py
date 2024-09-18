from django import forms
from .models import AddEvent, Comment

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
            'title', 'description', 'event_category', 'start_date_time',
            'end_date_time', 'location', 'is_free', 'price', 'link_to_event_page', 
            'excerpt', 'event_image'
        ]
        widgets = {
            'start_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'excerpt': forms.Textarea(attrs={'rows': 1, 'cols': 50}),  # Adjust size of form
        }
        """
        Help_texts display content under the field box
        """
        help_texts = {
            'title': 'Enter the event title. Make it catchy!',
            'description': 'Provide a detailed description of the event.',
            'event_category': 'Select the relevant category for this event.',
            'start_date_time': 'Specify the start date and time for the event.',
            'end_date_time': 'Specify the end date and time for the event.',
            'location': '"Optional" Enter the venue where the event will take place.',
            'is_free': '"Optional" Check if the event is free to attend.',
            'price': '"Optional" Specify the price if the event is not free.',
            'link_to_event_page': '"Optional" add a link to an external page.',
            'excerpt': '"Optional" Add a short summary or highlight of the event.',
            'event_image': 'Upload an image that represents the event.',
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class AttendForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())

