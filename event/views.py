from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
# use decorator for login users, add_event and my_event
from django.views import generic  # Django's generic views
from django.contrib import messages
# message framework, stores and displays temporary messages
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
    Displays all future events from :model:`event.AddEvent`.
    
    **Context**
    ``queryset`` All published future events.

    **Template**
    :template: `event/index.html`
    """
    queryset = AddEvent.objects.future_events()
    template_name = "event/index.html"
    paginate_by = 6


@login_required
def add_event(request):
    """
    Create a view that allows authenticated users to submit their events.
    @login_required will redirect to sign in page if not logged in
    Handles file uploads
    Allows authenticated users to create a new event using :model:`event.AddEvent`.

    **Context**
    ``form`` An instance of :form:`event.AddEventForm`.

    **Template**
    :template: `event/add_event.html`
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
                request, messages.SUCCESS, "Add event request received!"
                " It will be reviewed within 2 days.")
            return redirect('home')  # Redirect to the home page
    else:
        form = AddEventForm()

    return render(request, 'event/add_event.html', {'form': form})


# edit event
def edit_event(request, slug):
    """
    Allows a user to edit an existing event from :model:`event.AddEvent`.

    **Context**
    ``event`` The event instance being edited.
    ``form`` An instance of :form:`event.AddEventForm`.

    **Template**
    :template: `event/add_event.html`
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
    """
    The event and the form are passed to the add_event.html template.
    This template will display the form with the pre-filled data for
    the user to edit.
    """


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
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return redirect('home')
    # return HttpResponseRedirect(reverse('addevent_detail', args=[slug]))


@login_required
def my_events(request):
    """
    Users can view and manage their own events,
    It lists only the events created by this logged-in user, including drafts.
    @login_required will redirect to sign in page if not logged in
    Displays the current user's events from :model:`event.AddEvent`.

    **Context**
    ``events`` A list of events created by the user.

    **Template**
    :template: `event/my_events.html`
    """
    events = AddEvent.objects.filter(organiser=request.user)
    return render(request, 'event/my_events.html', {'events': events})


def addevent_detail(request, slug):
    """
    Displays the details of a specific event from :model:`event.AddEvent`,
    along with comments and attendance information.

    **Context**
    ``addevent`` The event instance.
    ``comments`` List of event comments.
    ``comment_form`` A form to submit new comments.
    ``user_attending`` Boolean indicating if the user is attending.
    ``attending_count`` Number of users attending the event.

    **Template**
    :template: `event/addevent_detail.html`
    """
    # Fetch published events and drafts for the organizer
    addevent = get_object_or_404(AddEvent, slug=slug)

    # Check if the event is a draft and the user is not the organiser
    if addevent.status == 0 and addevent.organiser != request.user:
        return render(request, "404.html")  # Show 404 for non-organizers

    # Fetch comments and attendance info
    comments = addevent.comments.all().order_by("-created_at")
    comment_count = addevent.comments.filter(is_approved=True).count()

    user_attending = (
        request.user.is_authenticated and addevent.attendees.filter(
            attending_user=request.user).exists()
    )
    """
    if the user is logged in, get all the attendance records for that event.
    The attendees filter sees if the current user matches any objects in
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

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
    """
    Renders the calendar view page.

    **Context**
    No additional context.

    **Template**
    :template: `event/calendar.html`
    """
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
    Displays a paginated list of events filtered by category
    from :model:`event.AddEvent`.

    **Context**
    ``category`` The selected category.
    ``object_list`` The filtered list of events.

    **Template**
    :template: `event/events_by_category.html`
    """
    model = AddEvent
    template_name = 'event/events_by_category.html'
    paginate_by = 6

    def get_queryset(self):
        """
        A custom queryset.
        The default ListView queryset would return all objects of the
        specifiied model. Now customised to filter events by category
        self.kwargs['category_id'] will extract the category_id from the URL
        """
        category = get_object_or_404(Category, id=self.kwargs['category_id'])
        self.category = category
        # Store the category in self.category variable
        return get_filtered_events_by_category(category)
        # using the earlier function for categories and future events

    def get_context_data(self, **kwargs):
        """
        Adds the category to the context dictionary
        super() called parents class .get_context_data, the id
        Adds the variable self.category to context dictionary under
        the key 'category'
        """
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        # self.category is category variable above
        return context


def comment_edit(request, slug, comment_id):
    """
    Allows a user to edit their comment on an event
    from :model:`comment.Comment`.

    **Template**
    No template rendered. Redirects to event detail page.
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
            messages.add_message(
                request, messages.SUCCESS, 'Comment Updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('addevent_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Allows a user to delete their comment from :model:`comment.Comment`.
    """
    queryset = AddEvent.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('addevent_detail', args=[slug]))


def toggle_attendance(request):
    """
    Toggles the attendance status of the current user for a specific event
    from :model:`event.AddEvent`.
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
