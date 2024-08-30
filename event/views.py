from django.shortcuts import render
from django.views import generic 
from .models import AddEvent

# Create your views here.
class EventList(generic.ListView): 
    """
    All events in the database are displayed
    This ListView is a generic django view
    Displaying events from the AddEvent model
    """
    queryset = AddEvent.objects.all() # Gets all 'AddEvent' objects from the database and sends them to the template.
    # template_name = "addevent_list.html" # Specifies the template that should be rendered
    template_name = "event/index.html"
    paginate_by = 6