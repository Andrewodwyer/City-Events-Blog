from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
# use decorator for login users
from django.views import generic  # Django's generic views
from django.contrib import messages
# message framework, stores and displays tempory messages
from django.http import JsonResponse  # converts data to JSON
from django.http import HttpResponseRedirect
# Redirects the user to a different URL after performing the action.
from slugify import slugify  # change titles to slug
from .models import AddEvent, Category, Comment, Attending
# Import the AddEvent, Category, Comment model
from .forms import AddEventForm, CommentForm
# function taken from the forms.py file


# Create your views here.
class EventList(generic.ListView):
    """
    All events in the database are displayed
    This ListView is a generic django view
    Displaying events from the AddEvent model
    .future_events() comes from the AddEventManager class in the models.py
    It filters on time and has a status of 1 (published)
    """
    queryset = AddEvent.objects.future_events()
    # Gets all 'AddEvent' objects from the database and sends them
    # to the template.
    template_name = "event/index.html"
    paginate_by = 6
    # paginate by 6 tells Django to display 6 posts at a time


def add_event(request):
    """
    Create a view that allows authenticated users to submit their events.
    Handles file uploads
    """
    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            event = form.save(commit=False)  # Do not save to the database yet
            event.organiser = request.user
            # Set the current user as the organiser
            event.status = 0  # Mark event as "Draft" by default

            # Automatically generate the slug from the title. slugify
            event.slug = slugify(event.title)

            event.save()  # Save the event to the database
            messages.add_message(
                request, messages.SUCCESS, "Add event request received! It will be reviewed within 2 days.")
            return redirect('home')  # Redirect to the home page
    else:
        form = AddEventForm()

    return render(request, 'event/add_event.html', {'form': form})

# edit event


def edit_event(request, slug):
    """
    It fetches the event that the user wants to edit.
    It uses the slug passed in the URL to find the specific
    event in the AddEvent model.
    """
    event = get_object_or_404(AddEvent, slug=slug)

    if request.method == 'POST':
        form = AddEventForm(request.POST, request.FILES, instance=event)
        """
        request.FILES A dictionary, where each key corresponds to the name
        of a file input field in the HTML form, crispyform
        instance=event update this specific instance with the new data
        from the form.
        """

        if form.is_valid():
            form.save()
            # update the existing event
            messages.success(request, 'Event updated successfully!')
            return redirect(reverse('addevent_detail', args=[slug]))
            # Redirect to the event detail page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AddEventForm(instance=event)
        # populates the form with the existing data using instance=event

    context = {
        'event': event,
        'form': form
    }
    return render(request, 'event/add_event.html', context)
    # Use the add_event.html template. The event and the form are passed to the add_event.html template.
    # This template will display the form with the pre-filled data for the user to edit.


def delete_event(request, slug, event_id):
    """
    Get an event by it's primary key, event_id
    If the request came from the event organiser(addevent field), delete.
    """

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
    It lists only the events created by this logged-in user, including drafts.
    """
    events = AddEvent.objects.filter(organiser=request.user)
    return render(request, 'event/my_events.html', {'events': events})


def addevent_detail(request, slug):
    """
    Display an individual event, only the organizer can view draft events.
    """
    # Fetch published events and drafts for the organizer
    addevent = get_object_or_404(AddEvent, slug=slug)

    # Check if the event is a draft and the user is not the organizer
    if addevent.status == 0 and addevent.organiser != request.user:
        return render(request, "404.html")  # Show 404 for non-organizers

    # Fetch comments and attendance info
    comments = addevent.comments.all().order_by("-created_at")
    comment_count = addevent.comments.filter(is_approved=True).count()

    user_attending = request.user.is_authenticated and addevent.attendees.filter(attending_user=request.user).exists()
    """
    if the user is logged in, get all the attendance records for that event.
    The attendees he filter sees if the current user matches any objects in
    the attending_user field of Attending model
    It exists() if it matches the filter
    """
    attending_count = Attending.objects.filter(event=addevent).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.event = addevent
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(
        request, "event/addevent_detail.html",
        {"addevent": addevent,
         "comments": comments,
         "user_attending": user_attending,
         "attending_count": attending_count,
         "comment_count": comment_count,
         "comment_form": comment_form, }
    )


def get_events(request):
    """
    This will retrieve all events from the AddEvent model
    After the loop finishes building the events_list,
    the function returns it as a JSON response using Django JsonResponse
    FullCalendar can use JSON to display events in the calendar
    """
    events = AddEvent.objects.filter(status=1)
    # Fetch Published events from AddEvent model
    events_list = []
    # Create a list of events in the format required by FullCalendar

    for event in events:
        """
        The for loop adds title and start(date) to the event_list array
        for the FullCalendar to use
        """
        events_list.append({
            'title': event.title,
            'start': event.start_date_time.isoformat(),
            # FullCalendar expects date in ISO format
            'url': f'/event/{event.slug}/',
            # Provide the URL to the event detail page
        })

    return JsonResponse(events_list, safe=False)


def calendar_view(request):
    return render(request, 'event/calendar.html')


def get_filtered_events_by_category(category):
    """
    Filters current or future events first
    Filtering by Category next.
    The .future_events() from the model
    """
    return AddEvent.objects.future_events().filter(event_category=category)


class EventListByCategory(generic.ListView):
    """
    Using Djangos ListView it will show the model (AddEvent) in the template
    (events_by_category.html) paginated by 6.
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
        return get_filtered_events_by_category(category)
        # using the earlier function for categories and future events

    def get_context_data(self, **kwargs):
        """
        Adds the category to the context dictionary
        super() called parents class .get_context_data, the id
        Adds the variable self.category to context dictionary under the key 'category'
        """
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        # self.category is category variable above
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
    """
    The user attending status
    """
    if request.method == 'POST':
        #  If the request is post
        event_id = request.POST.get('event_id')
        # get the event_id, the relevant event
        event = get_object_or_404(AddEvent, id=event_id)
        # The AddEvent object with the specified id, event_id is retrieved

        # Check if the user is already attending the event via Attending model
        attendance, created = Attending.objects.get_or_create(
            # attendance = true, created = false.
            # get_or_create method on the Attending model to see if the
            # attendance record already exists
            attending_user=request.user,
            # for the current user
            # if no record exist, a new one is created and created is now true
            event=event

        )

        if not created:
            # If the object already exists, user is already attending, delete
            attendance.delete()
            attending = False
        else:
            # If created, the user was not attending and now is
            attending = True

        # Return updated attendance status and count
        return JsonResponse({
            'user_attending': attending,
            'attending_count': Attending.objects.filter(event=event).count()
            # querying the Attending model of all records in that event_id
            # returns a JSON response with new attendance status and the count
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
