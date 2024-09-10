from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required #use decorator for login users
from django.views import generic 
from django.http import JsonResponse
# from django.core.paginator import Paginator #add pagination to list view
from .models import AddEvent, Category # Import the AddEvent model
from .forms import AddEventForm # function taken from the forms.py file

# Create your views here.
class EventList(generic.ListView): 
    """
    All events in the database are displayed
    This ListView is a generic django view
    Displaying events from the AddEvent model
    """
    queryset = AddEvent.objects.all() # Gets all 'AddEvent' objects from the database and sends them to the template.
    template_name = "event/index.html"
    paginate_by = 6
    # paginate by 6 tells Django to display 6 posts at a time


@login_required
def add_event(request):
    """
    Create a view that allows authenticated users to submit their events.
    Handles file uploads also
    """
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            event = form.save(commit=False)
            event.organiser = request.user  # Set the current user as the organiser
            event.status = 0  # Mark event as "Draft" by default
            event.save()
            return redirect('home')  # Redirect to the home page after submission
    else:
        form = AddEventForm()
    
    return render(request, 'event/add_event.html', {'form': form})

@login_required
def my_events(request):
    """
    Users can view and manage their own events,
    It lists only the events created by this logged-in user
    """
    events = AddEvent.objects.filter(organiser=request.user)
    return render(request, 'my_events.html', {'events': events})


def addevent_detail(request, slug):
    """
    Display an individual :model:`event.AddEvent`.

    **Context**

    ``addevent``
        An instance of :model:`event.AddEvent`.

    **Template:**

    :template:`event/addevent_detail.html`
    """

    queryset = AddEvent.objects.filter(status=1)
    addevent = get_object_or_404(queryset, slug=slug)

    return render(
        request, "event/addevent_detail.html", {"event": addevent,},
    )

def get_events(request):
    """
    This will retrieve all events from the AddEvent model
    After the loop finishes building the events_list,
    the function returns it as a JSON response using Django JsonResponse
    FullCalendar can use JSON to display events in the calendar
    """
    events = AddEvent.objects.all()  # Fetch events from AddEvent model
    # Create a list of events in the format required by FullCalendar
    events_list = []

    for event in events:
        # The for loop adds title and start(date) to the event_list array for the FullCalendar to use
        events_list.append({
            'title': event.title,
            'start': event.start_date_time.isoformat(),  # FullCalendar expects date in ISO format
            'url': f'/event/{event.slug}/',  # Provide the URL to the event detail page
        })

    return JsonResponse(events_list, safe=False)

def calendar_view(request):
    return render(request, 'event/calendar.html')

def event_list_by_category(request, category_id):
    """
    Filtering by Category. Passes the selected category to the view and filter the AddEvent objects.
    This view function response/return, renders a template (HTML file) and sends it back to the users browser
    using this format render(request, template_name, context=None, content_type=None, status=None, using=None)
    context: This is a dictionary containing data i want to pass to the html template.
    """
    category = get_object_or_404(Category, id=category_id)
    events = AddEvent.objects.filter(event_category=category)
    return render(request, 'event/events_by_category.html', {'category': category, 'events': events})

def event_list(request):
    event_list = AddEvent.objects.all()
    paginator = Paginator(event_list, 6)
    # Get the current page number from the request
    page_number = request.GET.get('page', 1)
    events = paginator.page(page_number)
    return render(request, 'event/events_by_category.html', {'events: events'})


class EventListByCategoryView(generic.ListView):
    model = AddEvent
    template_name = 'event/events_by_category.html'  # The template that will display the events
    context_object_name = 'events'  # The name of the object list in the template (optional, default is 'object_list')
    paginate_by = 6  # Number of events to display per page

    def get_queryset(self):
        """
        Override the get_queryset method to filter the events by category.
        """
        category_id = self.kwargs.get('category_id')
        return AddEvent.objects.filter(event_category_id=category_id)

# def homepage(request):
#     categories = Category.objects.all()
#     return render(request, 'index.html', {'categories': categories})

