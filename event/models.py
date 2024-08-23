from django.db import models
from django.contrib.auth.models import User
"""
A draft zero and published is one, default is to save as a draft
"""
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Category model for EventCategory ForeignKey
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# AddEvents model
class AddEvents(models.Model):
    """
    Stores a single event post related to :model:`auth.User`.
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event_image = CloudinaryField('event_image', default='placeholder')
    organiser = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="event_addevent"
    )  # ForeignKey to User model
    description = models.TextField()
    event_category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Category model
    start_date_time = models.DateTimeField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link_to_event_page = models.URLField(max_length=1024)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['start_date_time']  # Orders by start_date_time in ascending order (soonest first)

    def __str__(self):
        return f"{self.title} | organised by {self.author}"