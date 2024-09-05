from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone #local time 

"""
A draft zero and published is one, default is to save as a draft
"""
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Category model for EventCategory ForeignKey
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Event Category" #to use instead of class name in admin panel
        verbose_name_plural = "Event Categories"

    def __str__(self):
        return self.name

# AddEvent model
class AddEvent(models.Model):
    """
    Stores a single event post related to :model:`auth.User`.
    """
    title = models.CharField(max_length=255, unique=True)
    # slug is a semantic URL path rather than an integer or database row ID
    slug = models.SlugField(max_length=200, unique=True)
    # event_image = CloudinaryField('event_image', default='placeholder')
    organiser = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="event_addevent"
    )  # ForeignKey to User model
    description = models.TextField()
    event_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events', default=1)
    # ForeignKey to Category model, Default=1 is the id for Music
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField(default=timezone.now)
    location = models.CharField(blank=True)
    is_free = models.BooleanField(default=False)  # Add a free option
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True) #price can be blank
    link_to_event_page = models.URLField(max_length=1024, blank=True)
    status = models.IntegerField(choices=STATUS, default=0) 
    # integerField is a number picker but is overridden to a string drop down
    excerpt = models.TextField(blank=True)  # Optional summary or preview of the posted event
    updated_on = models.DateTimeField(default=timezone.now) #sets the time the event was created
    # Add Cloudinary image field
    event_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['start_date_time']  # Orders by start_date_time in ascending order (soonest first)
        verbose_name = "Add Event"
        verbose_name_plural = "Add Events"

    def __str__(self):
        return f"{self.title} | organised by {self.organiser}"

# Comment model for user comments on events
class Comment(models.Model):
    event = models.ForeignKey(AddEvent, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False) # requires admin approval

    class Meta:
        ordering = ["created_at"] # newest first

    def __str__(self):
        return f'Comment {self.content} by {self.user.username} on {self.event.title}'


# Attending model to track which users are attending which events
class Attending(models.Model):
    """ 
    Stores the User that is attending
    User is foreign key for the attending_user. 
    AddEvents is the foreign key for the event.
    on_delete=models.CASCADE will delete all indications 
    of attending if user is deleted
    """
    attending_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_attending')
    event = models.ForeignKey(AddEvent, on_delete=models.CASCADE, related_name='event_attendees')
    timestamp = models.DateTimeField(default=timezone.now)  # Automatically records when the user attends

    class Meta:
        unique_together = ('attending_user', 'event')  # Ensure a user can attend the same event only once
        ordering = ['-timestamp']  # Newest attendance first
        verbose_name = "User Attending"
        verbose_name_plural = "Users Attending"

    def __str__(self):
        return f'{self.attending_user.username} attending {self.event.title}' #for the admin panel. to easly know which post is which

