from django import forms
from .models import AddEvent, Comment
from django.core.exceptions import ValidationError
from django.utils import timezone  # for comparing the current time
from datetime import timedelta


class AddEventForm(forms.ModelForm):
    class Meta:
        """
        Meta data give information to the form, Which model
        it is and a list of fields that will be in the form.
        The widgets dictionary allows overriding the default
        Django behavior by specifying exactly how the fields
        are to be rendered in the form.
        attrs parameter allows me to specify the HTML attributes
        type': 'datetime-local is more user friendly and allow for
        both date and time in the 1 field
        """
        model = AddEvent
        fields = [
            'title', 'description', 'event_category', 'start_date_time',
            'end_date_time', 'location', 'is_free', 'price',
            'link_to_event_page', 'excerpt', 'event_image'
        ]
        widgets = {
            'start_date_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
            'end_date_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local'}),
            'excerpt': forms.Textarea(attrs={'rows': 1, 'cols': 50}),
            # Adjust size of form
        }
        help_texts = {
            'title': 'Enter the event title. Make it catchy!',
            'description': 'Provide a detailed description of the event.',
            'event_category': 'Select the relevant category for this event.',
            'start_date_time': 'Select a start date and time for the event.',
            'end_date_time': 'Specify the end date and time for the event.',
            'location': '"Optional" Enter the venue name and location',
            'is_free': '"Optional" Check if the event is free to attend.',
            'price': '"Optional" Specify the price if the event is not free.',
            'link_to_event_page': '"Optional" add a link to an external page.',
            'excerpt': '"Optional" Add a short summary of the event.',
            'event_image': 'Upload an image that represents the event.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set input formats to match HTML5 datetime-local format
        self.fields['start_date_time'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['end_date_time'].input_formats = ['%Y-%m-%dT%H:%M']

    def clean_start_date_time(self):
        """
        Ensure that the start date is in the future is round to
        minute precision.
        """
        start_date_time = self.cleaned_data.get('start_date_time')

        if start_date_time:
            # Round seconds down to the nearest minute
            start_date_time = start_date_time.replace(second=0, microsecond=0)
            if start_date_time <= timezone.now():
                raise ValidationError(
                    "The start date and time must be in the future."
                    )
        return start_date_time

    def clean_end_date_time(self):
        """
        Ensure that the end date is after the start date are
        round to minute precision.
        """
        end_date_time = self.cleaned_data.get('end_date_time')
        if end_date_time:
            # Round seconds down to the nearest minute
            end_date_time = end_date_time.replace(second=0, microsecond=0)
        return end_date_time

    def clean(self):
        """
        Ensure that end date is after start date.
        """
        cleaned_data = super().clean()
        start_date_time = cleaned_data.get('start_date_time')
        end_date_time = cleaned_data.get('end_date_time')

        if start_date_time and end_date_time:
            if end_date_time <= start_date_time:
                raise ValidationError(
                    "End date & time must be after the start time."
                    )
        return cleaned_data


class CommentForm(forms.ModelForm):
    """
    a form that allows user to input content for a comment.
    linked to the Comment model in the database
    """
    class Meta:
        model = Comment
        fields = ('content',)
