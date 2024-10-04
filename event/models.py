from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # use cloudinary for images
from django.utils import timezone  # local time


"""
A draft zero and published is one, default is to save as a draft
"""
STATUS = ((0, "Draft"), (1, "Published"))


# Category model


class Category(models.Model):
    """
    Stores categories. Foreign key field event_cateory
    in :model:`event.AddEvent`.
    """
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Event Category"
        # to use instead of class name in admin panel
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return self.name


class AddEventManager(models.Manager):
    """
    Not a model
    Custom manager for the :model:`event.AddEvent` model.
    Provides future event filtering through
    the `future_events()` method.
    This is a custom manager seperate to all() etc
    models.Manager extends Djangos base models.Manager.
    """
    def future_events(self):
        """
        Looks at the filed start_date_time, then used gte to see
        if it greater or equal to the timezone.now() filter and
        if so, gives it a status of 1 gte: greater than or equal to
        This function future_events is used in EventList and
        get_filtered_events_by_category in the view
        Only published events
        """
        return self.filter(
            start_date_time__gte=timezone.now(), status=1)


class AddEvent(models.Model):
    """
    AddEvent model
    Stores a single event entry related to :model:`auth.User`
    and :model:`event.Category`.
    Includes a custom manager to filter events
    based on date and status.
    """
    title = models.CharField(max_length=255, unique=True)
    # slug is a semantic URL path rather than an integer or database row ID
    slug = models.SlugField(max_length=200, unique=True)
    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_addevent")
    # ForeignKey to User model
    description = models.TextField()
    event_category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='events', default=1
        )
    # ForeignKey to Category model, Default=1 is the id for Music
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(blank=True)
    is_free = models.BooleanField(default=False)  # Add a free option
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True)
    # price can be blank
    link_to_event_page = models.URLField(max_length=1024, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # Draft =0 Published=1
    # integerField is a number picker but is overridden to a string drop down
    excerpt = models.TextField(blank=True)
    # Optional summary or preview of the posted event
    updated_on = models.DateTimeField(default=timezone.now)
    # sets the time the event was created
    # Add Cloudinary image field
    event_image = CloudinaryField('image', default='placeholder')

    # Use the custom manager
    objects = AddEventManager()

    class Meta:
        ordering = ['start_date_time']
        # Orders by start_date_time in ascending order (soonest first)
        verbose_name = "Add Event"
        verbose_name_plural = "Add Events"

    def __str__(self):
        return f"{self.title} | organised by {self.organiser}"

# Comment model for user comments on events


class Comment(models.Model):
    """"
    Stores a single comment related to :model:`event.AddEvent`
    and :model:`auth.User`.
    Requires admin approval before being visible.
    """
    event = models.ForeignKey(
        AddEvent, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    # requires admin approval

    class Meta:
        ordering = ["created_at"]  # newest first

    def __str__(self):
        return f'Comment {self.content} by {self.user.username} on {
            self.event.title}'


# Attending model to track which users are attending which events
class Attending(models.Model):
    """
    Tracks attendance of users for events,
    related to :model:`event.AddEvent` and :model:`auth.User`.
    Ensures unique attendance per event for each user.
    AddEvents is the foreign key for the event.
    on_delete=models.CASCADE will delete all indications
    of attending if user is deleted
    """
    attending_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='User_attending')
    event = models.ForeignKey(
        AddEvent, on_delete=models.CASCADE, related_name='attendees'
        )
    timestamp = models.DateTimeField(default=timezone.now)
    # Automatically records when the user attends

    class Meta:
        unique_together = ('attending_user', 'event')
        # Ensure a user can attend the same event only once
        ordering = ['-timestamp']  # Newest attendance first
        verbose_name = "User Attending"  # for admin panel
        verbose_name_plural = "Users Attending"

    def __str__(self):
        return f'{self.attending_user.username} attending {self.event.title}'
        # for the admin panel. to easily know which post is which
