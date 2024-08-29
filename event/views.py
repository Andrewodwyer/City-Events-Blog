from django.shortcuts import render
from django.views import generic
from .models import AddEvent

# Create your views here.
class EventList(generic.ListView): 
    """
    All events in the database are displayed
    This ListView is a generic django view
    """
    queryset = AddEvent.objects.all() 
    template_name = "addevent_list.html"