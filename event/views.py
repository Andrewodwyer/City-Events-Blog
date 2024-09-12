from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required #use decorator for login users
from django.views import generic 
from django.contrib import messages
from django.http import JsonResponse
# from django.core.paginator import Paginator #add pagination to list view
from django.http import HttpResponseRedirect
from .models import AddEvent, Category, Comment # Import the AddEvent, Category, Comment model
from .forms import AddEventForm # function taken from the forms.py file
from .commentforms import CommentForm

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
            event = form.save(commit=False)  # Do not save to the database yet
            event.organiser = request.user  # Set the current user as the organiser
            event.status = 0  # Mark event as "Draft" by default
            
            # Automatically generate the slug from the title
            event.slug = slugify(event.title)
            
            event.save()  # Save the event to the database
            messages.add_message(request, messages.SUCCESS, "Add event request received! It will be reviewed within 2 days.")
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
    status=1 selects the published events, status=0 is draft and admin publishes them
    ``addevent``
        An instance of :model:`event.AddEvent`.

    **Template:**

    :template:`event/addevent_detail.html`
    """

    queryset = AddEvent.objects.filter(status=1) 
    addevent = get_object_or_404(queryset, slug=slug)
    comments = addevent.comments.all().order_by("-created_at")
    comment_count = addevent.comments.filter(is_approved=True).count()
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # is_valid() has it been fill in correctly
            comment = comment_form.save(commit=False)
            # .save() save to the database, comment=False returns an object that hasn't been save
            comment.user = request.user
            # request.user is the logged in user, relating current user to comments model field user
            comment.event = addevent
            comment.save()
            # comments now saved
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
                # messages to be used in base.html
    )

    comment_form = CommentForm()
    print("About to render template")

    return render(
        request, "event/addevent_detail.html", 
        {"event": addevent,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
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
    """
    Displays all the events in a page with pagination set to 6.
    first page set to page 1 
    """
    event_list = AddEvent.objects.all()
    paginator = Paginator(event_list, 6)
    page_number = request.GET.get('page', 1)
    # Get the current page number from the request
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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

