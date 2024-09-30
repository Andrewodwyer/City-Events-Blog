![The Work Logo](static/readme-img/favicon.ico)

# THE WORD 

[Andy O'Dwyer](https://github.com/Andrewodwyer)

# Live App

[Link to THE WORD site](https://events-blog-f44bf5c7d7d5.herokuapp.com/)

City events website.

<hr>
The Work is an events website where a registered user can input events and also indicate if they will attend other events. Users will be able to search by categories with a nav bar dedicated to 4 different categories. They can also view events by dates in a calendar. Registered users have 4 additional options over none registered users. 

- Create an event
- View their events, Draft and published
- leave a comment
- Indicate attendance
- All of which have CRUD functionality

<hr>

![Am I Responsive Image](static/readme-img/amiresponsive.png)

## UX

### Target Audience

The Word’s events platform is designed for people who are interested in discovering, attending, and organising local and online events. The app concept is like a bulletin board in a shop or office space. People can post and see events in the local area. In the same way this site encourages users to both search for events and post their own events. 

The Word is geared to both casual event attendees and engaged organisers / registered users, providing a platform that encourages social engagement and participation.

Information on users:
Age:The apps expected user will be over 18, due to a lot of music venues having age restrictions.
Location: The intention of the app is to have one for each city e.g THE WORD Cork/Waterford/Dublin/Limerick etc. In this way the user will utilise an app relevant to their location.

Users interests in finding information in numerous categories
- Music
- Sport
- Classes
- Culture

The registered user or organiser is interested in creating and managing their own events, either as a hobby or professional service.

#### How people will use the app:

- None Registered Users
  - 1 Users who are interested in seeing local events, what’s on now and in the future.
  - 2 Users that want to search by a certain category, Music, Sports, Classes and Culture. 
  - 3 People that want to choose an event by a certain date. Viewing upcoming events on a calendar.

- Registers Users
  They will have the same abilities as the none registered users plus the following
  - 4 Add their own event
  - 5 Update and delete their event
  - 6 See a list of event they’ve created
  - 7 Indicate if they will be attending an event
  - 8 Write a comment on an event
  - 9 Edit and delete their comment



#### Why users will use the app:

-  Search flexibility: 
  - Users can easily search for events through categories (music, sports, classes, culture) and dates, improving event discoverability.

-  Event attendance: 
  - Registered users can indicate whether they plan to attend an event, which enhances event visibility and participation.
  - Organiser can also track interest

  - User-generated content: 
    - The site allows users to create, read, edit and delete their own events. They have the ability to create events and manage details like location, time, and description.

  - Engagement through comments: 
    - Registered users can leave comments on event pages, encouraging engagement and conversation around events.

### User Goals

For Attendees: 
- Users primarily visit The Word to discover new events that match their interests and schedule.
- They want a streamlined way to browse events, show attendance, and possibly engage in discussions with other attendees.


For Organisers: 
- Users who create events are looking for an easy way to promote their events, manage their listings, and interact with potential attendees. The platform’s CRUD (Create, Read, Update, Delete) functionality provides them with the flexibility to create, edit, or remove events as needed. Giving them full control over their event.

### User Stories
The user stories are available on the kanban board and some will be discussed in the EPics below.
There as three main users
- Admin: This is the site owner that will have full control over the publishing of events, and comments.
- Registered Users: User and organisers who are logged, allowing for more functionality 
- Non-registered users: limited functionality
These users have been groupled in the kanban board with tags and their user stories have been given epics for each type of user

## Kanban

For this project I created a Kansan board in GitHub to display the stages and status of each user-story. I assigned priority to each user-story using the MoSCoW method. The User-story were grouped into Epics and each User-story was given a Story Point using the T-shirt Sizing method. 

### Kanban boards in github project:
- MoSCow Prioritisation
- Epics to group user-stories
- Story Points: to estimate the work required
- Status: What stage it’s on.

### MoSCow Prioritisation

##### M: Must Have
 - Non-negotiable product needs that are mandatory.
 - Deciding factors for Must haves: 
What will happen if this is not included
Is there a simpler way to accomplish this?
Will the product work without it?

##### S. Should-have
-  They are essential to the product/project but they are not vital. The product will still function without it. However, the addition will add significant value. They can be scheduled for a future date.

##### C. Could-haves 
-  Nice to haves. Not necessary to the core function. They have a much smaller impact on the outcome if left out. They will be the first to be deprioritised.

##### W. Will not have
- This manages expectations and prevents scope creep. They are not expected in this specific time frame.

![MoSCoW Prioritisation](static/readme-img/Agile/MoSCoW.png)


## Epics

In a Kanban board, an epic is a large body of work that can be broken down into multiple smaller user stories and tasks. Each epic generally corresponds to a specific area. The epics are organised by three types of users in the system: Admin, Registered Users, and Non-Registered Users.

Below is a description of each epic based on the user roles in your system:

#### Epic 1: Admin

This epic groups together all the functionality and user stories related to the Admin role. The Admins are users who have the highest level of access and can manage various aspects of the app. Their stories will involve managing users, events, comments and who is attending each event. 
- Abilities:
  -	Admins can create, edit, or delete user accounts
  -	Admins can create, approve, edit, and delete events, comments and attendance submitted by registered users.
  -	Admins have the ability to review user-generated content (e.g., events, comments, or attendance) and edit/delete if required.

- Example User Stories:
  -	“As the Admin I can view event request and comment requests, so that I can review and approve them”
  -	“As an Admin, I want to approve or reject registered users publishing events so that only verified events are added to the app”

#### Epic 2: Registered User

This epic encompasses all the features and interactions available to Registered Users. These users have accounts and have increase abilities over non-registered users.
- Abilities:
  -	Registered users can create new events and submit them for admin approval.
  - Registered users can view, show attendance, and write comments on events.
  -	My Events: Registered users can see the events they've created.
  - They have CRUD functionality
    - Adding an event (editing the event),
    - Writing a comment (edit the comment),
    - Show attendance (indicate attendance and also remove attendance)

- Example User Stories:
 - “As a user I can log in to my account so that I can add events, comment and indicate attendance”
 - “As a Registered User, I want to comment on events so that I can share my opinions or ask questions.”

#### Epic 3: Non-Registered User

This epic covers the functionality accessible to Non-Registered Users, or users who visit the platform without signing up. These users have limited access compared to registered users but can still interact with the app to a certain degree.
- Abilities:
 - Event Browsing: Non-registered users can browse through public events without needing an account.
 - Category Search: Non-registered users can search for events based on categories and dates in the calendar
 - View Event Details: Non-registered users can view the full details of a specific event, including descriptions, dates, locations, and organiser information.
 - Limited Interaction: While non-registered users cannot create or participate in events, they can view event information and are prompted to sign up for further actions.

- Example User Stories:
	- “As a user I can open a event listing from the calendar so that see more details of the event”
	- “As a User, I want to browse and search for events so that I can find events that interest me.”

Each of these epics groups together the relevant user stories under a common theme, making it easier to manage and visualize progress on your Kanban board. The Epics are grouped using Tags on the User Stories eg. Tag: "Epic 1: Registered Users"

![Kanban Board](static/readme-img/Agile/Kanban-Board.png)

[View Kanban Board here](https://github.com/users/Andrewodwyer/projects/6)


## Agile Story points in Scrum

Story points are a unit of measure used in Agile project management in Scrum, to estimate the relative effort or complexity of user stories or backlog items.
Instead of estimating in terms of time (e.g., hours or days), which can be subjective and vary based on individual team members’ skill levels, story points focus on the overall effort or complexity involved. Story points represent a combination of factors, including the effort required, technical complexity, risks, and dependencies.I have used T-shirt Sizing for this.

- Some example of using Story Points:
	1.	User Story: “Manage My Own Posted Events” (Registered User)
	 - T-shirt Size: M (Medium), Story Points: 3
	 - Reason: A registered user managing their posted events involves creating, editing, or deleting events, which requires interaction with multiple parts of the system (the database, html, views etc.).

  2.	User Story: “View Comments” (Admin)
	 - T-shirt Size: XS (Extra Small), Story Points: 1
	 - Reason: For an admin, viewing comments is a read-only task with minimal complexity. The admin doesn’t need to interact with or modify the comments, making it a low-effort task that can be implemented quickly.

  3.	User Story: “View Calendar” (Non-Registered User)
	 - T-shirt Size: L (Large); 	Story Points: 5
	 - Reason: Viewing a calendar html and include events title based on dates. This involved an external library called FullCallendar. The make the events show in the calendar was a complex feature requiring significant development time, particularly in the use of JS, views and uls. JSONResponse was required.

By using T-shirt size Agile story points, you can effectively estimate the workload for each epic and user story

![Story Points Estimation](static/readme-img/Agile/T-shirt-size-story-points.webp)


## DRY principles:

#### Three main benefits: Reusability, Maintainability & Customisation

### HTML Template inheritance

#### base.html

base.html allows us to keep the look and feel of our site consistent. The header and the footer are constant throughout the entire website. Template inheritance goes hand in hand with DRY principles - Don't Repeat Yourself. Using inheritance, we only need to write them once. After that, we can inject the content from each page into named blocks. {% block content %}

This extends tag {% extends "base.html" %}  tells index.html that it is a child template of base.html. Then, everything we have inside our block fills the corresponding blocks in base.html, giving us a fully rendered web page.

We use this base.html for all pages to create the same look and feel for all our pages. The base.html template however is not the only one that can be reused. After writing each pages Html I saw there was other pages that could reuse code. There pages were
- index.html
- events_by_category.html
- my_events.html

#### Pagination:
Pagination is a fancy word meaning "divide up into pages”.
paginate_by = 6,  tells Django to display 6 posts at a time.
is_paginated is a boolean (set to true) more than the paginate number that was set to 6, add pagination. paginate number was set in the app view.py
    template_name = "event/index.html"
    paginate_by = 6
The key points to remember are the paginate_by setting in the view, and then the is_paginated boolean and page_obj object that is passed through to the template.
I first used this just on the index.html page. As the same pagination would be used on 3 html pages (index.html, events_by_category.html and my_events.html) I decided to place the pagination in its own template called pagination.html and include it in those 3 pages using the {%include%} tag.        
{% include "event/pagination.html" with page_obj=page_obj %}
The page_obj contains the current page’s events and pagination details of there is a next or previous

#### Event Card Display
Like the Pagination on these pages the majority of the code was the same. The only major difference was the h3 element at the start of the page and a message that displays at the end of the page if there is an if else statement {%if%}
The card_display.html template was created in response to this. This template used the code that was duplicated on each page. These pages are free of clutter and the card design need only be changed once in the event-card.html and would apply on all the relevant pages that had the {% include "event/event_card.html" with event=event %} tag.

![Pagination cards and buttons](static/readme-img/UX/pagination-6-card-and-button.png)



### Fontawesome and Bootstrap


##


## Bugs:
#### Category Migration 
-  I had to roll back the migrations from 0006 to 0003, using the terminal command
  python3 manage.py migrate events 0003 
  This was because I had set a default=“music” in the AddEvents model and had made a migration. The default had to be an integer so I checked what ID music had. This was done by using this command in the shell.
  from event.models import Category
  music_category = Category.objects.get(id=1)
  print(music_category.name)
  The result id was 1.
  I updated the code to reflect this. Below code, default=‘Music’ is now default=1
      event_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events', default=1)
  This still didn’t resolve the issue. When trying to make a migration using the integer 1 I was given an error of database is expecting a integer and instead got ‘Music’.
  I rolled back the migrations, deleted the last 2 migrations and made a new makemigration and migrate. 
  This resolved all the issues. I did have to set the categories in the admin panel again.

#### Load Static bug
-  I had used Django Template Language tag to include the images in the static directory for the events template html file but I didn’t do the same for the index.html file. Once I did this the images loaded as intended.

#### Categories in events bug
-  Fixed the bug in event_by_category.html, the loop was category in categories but it should of been events in events to show the events with the category_id, ie music has a category id of 1
  I used a function in the view.py called event_list_by_category and it got the Category object from the AddEvents 

#### Load Static in events_by_category.html bug
-  The static images on the events_by_category.html file weren’t loading and this gave me an error indicating it was expecting a {%endfor%} tag as it couldn’t see the static folder.
  This was easily fix by adding the {% load static %} tag at the top of the html file

#### Pagination for function based views Bug
-  Pagination for function based views. I was trying to add a function that used paginator = Paginator(events, 6). Because it was a function and not a generic class I had to add page_obj and is_paginated Django tags in a certain sequence. The issue was the page_obj wasn’t properly accessed in the template, which is causing the issue with the pagination displaying "Page of ." with no next or previous buttons. I consulted https://docs.djangoproject.com/en/5.1/topics/pagination/ and tried a number of different options but it didn’t work. In the EventList class the generic ListView automatically handles context variables like page_obj for pagination. I decided to use a generic list view class for the categories html template too.
  To have a simple class view I needed to set up a function that filtered the events by category and by current and future dates. For the dates I used the class AddEventManager(models.Manager): in the models.py that filtered by time. and set it’s status to 1 (published). Then I used the .filter(event_category=category) that got the category.

#### Loading Image in the index.html and then the addevent_detail.html
-  img src was different for index.html and addevent_details.html. This was because of the for loop {% for event in addevent_list %} in index which took the name addevent_list from the generic.ListView class EventList. While addevent_details.html used the variable name addevent. When I used the variable name addevent in the index.html it didn’t load because or the for loop. I decided to make a note of the issue and review it if needed.


#### Model issues: Comments and AddEvents user/organiser field Bug
-  In the AddEvents model I used ‘organiser’ as the field for the user. However in the Comment model the field was ‘user’ for the user and not ‘organiser’. This caused confusion when putting the conditional if and elif statements in the addevent_detail.html. In your template, I was using comment.organiser == user, but in my Comment model, the field that stores the user who created the comment is user, not organiser. To resolve this I replaced comment.organiser with comment.user. replaced comment.organiser  with comment.user.username to display the username of the comment. The edit button was the real issue and the change of comment.user == user so that it checks the user is the comment author.

#### URL pattern matching in urls.py. my-events path matching addevent_detail Bug
-  The path('event/<slug:slug>/', views.addevent_detail, name='addevent_detail') is being matched before path('event/my-events/', views.my_events, name='my_events'). Django matches the URLs in order from top to bottom, so when it saw event/my-events/, it treated "my-events" as a slug and tries to look up a corresponding AddEvent object, leading to the 404 error.
  To fix the issue I placed the event/my-events/ path before the event/<slug:slug>. So the more specific patterns (event/my-events) should come before less specific one.

#### Mixed Content bug
 - I was getting this error in the Issues section of Chrome inspect.
  Mixed Content: The page at '<URL>' was loaded over HTTPS, but requested an insecure element '<URL>'. This request was automatically upgraded to HTTPS, For more information see <URL>
  After researching and seeing a number of different articles, I found a fix on Slack. To fixed the mixed content i did the following. In settings.py file 
  ensure cloudinary uses https paths
  import cloudinary
  cloudinary.config(secure=True,)
  Thanks to tim_mentor for the code.

#### Summernote w3 validator error for <p> tag bug
-  Error: No p element in scope but a p end tag seen. Django Summernote.
  tim_mentor regarding issue
  It's a known bug that it adds extra paragraph tags to the body content in your posts. I think the same for the placeholders error?
  I’m aware of the issue/bug coming from Django Summernote.

#### My_events tab not Active when selected bug
-  I had added the my_events tab later then the other tabs in the nav as this was a could have in my list. I had added the link, DTL in the 'li' in the nav and the links worked bu the tab didn’t stay active. The issue was that the my_events_url was not defined in the base.html template using {% url ‘my_events” as my_events_url %}. Once I did this, it worked as expected.

#### FullCalendar and Django bug:
-  FullCalendar and Django are expecting different values for times. To resolve this a function was added to AddEventForm so the seconds are rounded down and both the front end and the backend receive the required information. 

#### FullCalendar Displaying all events and not just Published ones bug:
-  The views get_events collected all the events .all(). so it included the draft events that were not published by the admin. I needed to filter this my using the .filter(status=1) so only the status=1(Published) events are selected.

<hr>

## Future Features:

There is a number of additions that could be made to the app to increase it’s potential and appeal to users. 

- ### Develop the My_Events page to be more a profile page with more features:
  Currently the page shows the events created by the user/organiser. An added feature would be for a devision in this page. I column for created event  and a separate one for the events they’ve shown interest in, reserved seats for, shared events etc

- ### Reserve tickets:
  Similar to restaurant booking app, registers users could reserve a table or seat for an event. This feature would work well with most events, like workshops, seats at a concert etc

- ### Search bar:
  Add a search bar in the navigation menu to allow users to search for events using key words, some examples would be a venue name, a sub category, or event organiser. The search for organiser would be useful as they could be a venue that would have a number of events each week. This functionality not only saves time but also increases the likelihood of user satisfaction and retention.

- ### Sharing icon:
  Social Sharing & Friend Invites: Let users see what events their friends are attending and invite friends to join events, boosting community engagement.

- ### Favorites/Wish List: 
  Enable users to mark events as “favourites” or add them to a wish list. The user will be able to track these events on a personal page

- ### User Convenience: 
  Users can visually browse events based on proximity to their location
  Alongside filters, users can find events based on geographic areas.

- ### Event Reminders: 
  Reminders and calendar integration to help users remember to attend events they’ve indicated attendance.

- ### Share user comments: 
  As well as the share events, users can share their comments relation to an event.

- ### Event Reviews and Ratings:
  Allow attendees to leave a review and rating for the past event


### Validator Testing 

### HTML

[W3C validation](https://validator.w3.org/#validate_by_input) was used to check the markup validity of html file.

<details><summary><b>Home page, passed</b></summary>

![Home page](static/readme-img/code-validated/Home-index-html-checker.png)

</details>

<details><summary><b>Add/Create an Events page, passed</b></summary>

![Create an event](static/readme-img/code-validated/Add-event-html-checker.png)

</details>

<details><summary><b>Events Details, passed</b></summary>

![Event details](static/readme-img/code-validated/Event-details-html-checker.png)

</details>

<details><summary><b>Calendar page, passed</b></summary>

![Calendar page](static/readme-img/code-validated/Calendar-page-html-checker.png)

</details>

<details><summary><b>Events by category page, passed</b>Events by category page, passed</summary>

![Events by Category page](static/readme-img/code-validated/categories-html-checker.png)

</details>

<details><summary><b>My events page, passed</b></summary>

![My events page](static/readme-img/code-validated/my_events-html-checker.png)

</details>

<details><summary><b>Login page, passed</b></summary>

![Login page](static/readme-img/code-validated/Login-html-checker.png)

</details>

<details><summary><b>Sign up, 4 errors. Known summernote issues</b></summary>

![Sign up](static/readme-img/code-validated/Sign-up-html-checker.png)

</details>

<details><summary><b>logout page, passed</b></summary>

![Logout page](static/readme-img/code-validated/logout-html-checker.png)

</details>


### CSS

[Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check css files

<details><summary><b>style.css</b></summary>

![Logout page](static/readme-img/code-validated/css.png)

</details>

### JavaScript

[Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check css files

<details><summary><b>attendance.js</b></summary>

![attendance.js](static/readme-img/code-validated/attendance.js-check.png)

</details>

<details><summary><b>calendar.js</b></summary>

![calendar.js](static/readme-img/code-validated/calendar.js-checker.png)

</details>

<details><summary><b>eventsComments.js</b></summary>

![eventsComments.js](static/readme-img/code-validated/eventsComments.js-check.png)

</details>

### Python

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.

<details><summary><b>asgi.py</b></summary>

![Python](documentation/testing_files/asgi-python.png)
</details>

<details><summary><b>wsgi.py</b></summary>

![Python](documentation/testing_files/wsgi-python.png)
</details>

<details><summary><b>views.py (booking)</b></summary>

![Python](documentation/testing_files/views-booking-python.png)
</details>

<details><summary><b>urls.py</b></summary>

![Python](documentation/testing_files/apps-python.png)
</details>

<details><summary><b>forms.py</b></summary>

![Python](documentation/testing_files/test-forms-python.png)
</details>

<details><summary><b>models.py</b></summary>

![Python](documentation/testing_files/models-python.png)
</details>

<details><summary><b>admin.py</b></summary>

![Python](documentation/testing_files/admin-python.png)
</details>

<details><summary><b>apps.py</b></summary>

![Python](documentation/testing_files/apps-python.png)
</details>