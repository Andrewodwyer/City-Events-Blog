from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required #use decorator for login users
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from slugify import slugify
from .models import AddEvent, Category, Comment, Attending # Import the AddEvent, Category, Comment model
from .forms import AddEventForm, CommentForm # function taken from the forms.py file


# Create your views here.
class EventList(generic.ListView): 
    """
    All events in the database are displayed
    This ListView is a generic django view
    Displaying events from the AddEvent model
    .future_events() comes from the AddEventManager class in the models.py
    It filters on time and has a status of 1 (published)
    """
    queryset = AddEvent.objects.future_events() # Gets all 'AddEvent' objects from the database and sends them to the template.
    template_name = "event/index.html"
    paginate_by = 6
    # paginate by 6 tells Django to display 6 posts at a time


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
            
            # Automatically generate the slug from the title. python app called slugify
            event.slug = slugify(event.title)
            
            event.save()  # Save the event to the database
            messages.add_message(request, messages.SUCCESS, "Add event request received! It will be reviewed within 2 days.")
            return redirect('home')  # Redirect to the home page after submission
    else:
        form = AddEventForm()

    return render(request, 'event/add_event.html', {'form': form})

# edit event
def edit_event(request, slug):
    """
    It fetches the event that the user wants to edit.
    It uses the slug passed in the URL to find the specific event in the AddEvent model.

    """
    event = get_object_or_404(AddEvent, slug=slug)

    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect(reverse('addevent_detail', args=[slug]))  # Redirect to the event detail page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddEventForm(instance=event)
        # method of GET, populates the form with the existing data using instance=event

    context = {
        'event': event,
        'form': form
    }
    return render(request, 'event/add_event.html', context)
    # Use the add_event.html template. The event and the form are passed to the add_event.html template.
    # This template will display the form with the pre-filled data for the user to edit.



# def delete_event(request, slug):
#     event = get_object_or_404(AddEvent, slug=slug)

#     if request.user != event.organiser:
#         messages.error(request, 'You are not authorized to delete this event.')
#         return redirect('addevent_detail', slug=slug)

#     event.delete()
#     messages.success(request, 'Event deleted successfully!')
#     return redirect('home') 

#  New delete function
def delete_event(request, slug, event_id):

    event = get_object_or_404(AddEvent, pk=event_id)

    if request.user == event.organiser:
        event.delete()
        messages.add_message(request, messages.SUCCESS, 'Event deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return redirect('home')
    # return HttpResponseRedirect(reverse('addevent_detail', args=[slug]))    


# Look at this in the future
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

    # Check if the user is attending the event
    if request.user.is_authenticated:
        user_attending = addevent.attendees.filter(attending_user=request.user).exists() 
        # reverse relationships from the Attending model attendees to the event, related_name = attendees
    else:
        user_attending = False

    # Get the number of people attending
    attending_count = Attending.objects.filter(event=addevent).count()

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
        {"addevent": addevent,
        "comments": comments,
        "user_attending": user_attending,
        "attending_count": attending_count,
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
    # events = AddEvent.objects.all()  # Fetch all events
    return render(request, 'event/calendar.html') #{'events': events})


def get_filtered_events_by_category(category):
    """
    Filters current or future events first
    Filtering by Category next.
    The .future_events() from the model
    """
    return AddEvent.objects.future_events().filter(event_category=category)



class EventListByCategory(generic.ListView):
    """
    Using Djangos ListView it will show the model (AddEvent) in the template (events_by_category.html)
    paginated by 6.
    """
    model = AddEvent
    template_name = 'event/events_by_category.html'
    paginate_by = 6

    def get_queryset(self):
        """
        A custom queryset.
        The default ListView queryset would return all objects of the specifiied model.
        Now customised to filter events by category
        self.kwargs['category_id'] will extract the category_id from the URL
        """
        category = get_object_or_404(Category, id=self.kwargs['category_id'])
        self.category = category  # Store the category in self.category variable
        return get_filtered_events_by_category(category) #using the earlier function for categories and future events

    def get_context_data(self, **kwargs):
        """
        Adds the category to the context dictionary
        super() called parents class .get_context_data, the id
        Adds the variable self.category to context dictionary under the key 'category'
        """
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context



def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = AddEvent.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('addevent_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = AddEvent.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('addevent_detail', args=[slug]))


def toggle_attendance(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = get_object_or_404(AddEvent, id=event_id)

        # Check if the user is already attending the event via Attending model
        attendance, created = Attending.objects.get_or_create(
            attending_user=request.user,
            event=event
        )

        if not created:
            # If the object already exists, the user is already attending, so we remove
            attendance.delete()
            attending = False
        else:
            # If created, the user was not attending and now is
            attending = True

        # Return updated attendance status and count
        return JsonResponse({
            'user_attending': attending,
            'attending_count': Attending.objects.filter(event=event).count()
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
