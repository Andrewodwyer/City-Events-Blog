from django.db import models
from django.contrib.auth.models import User
"""
A draft zero and published is one, default is to save as a draft
"""
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class AddEvent(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="event_addevent"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
