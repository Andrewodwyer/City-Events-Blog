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

### Database Models

One of the first steps in producing this app was to design and implement custom models based on the information that users would want to store and access.

An entity relationship diagram was created as part of planning these custom models.

As you can see from the ERD, the relationships play a important role in how the information will be stored and accessed. Here are the main relationship and you'll also be able to view them in this Diagram

- Category model:
 - One-to-Many: A category can have many events (AddEvent model), but each event belongs to one category.

- AddEvent model:
 - One-to-Many: A single category can be associated with multiple events.
 - One-to-Many: A single user can create multiple events, but each event has one organiser.
 - One-to-Many: An event can have multiple comments, but each comment is linked to one event.

- Comments model:
 - One-to-Many: A single event can have many comments, but each comment is linked to one event.
 - One-to-Many: A single user can write many comments, but each comment is linked to one user.

- Attending model:
	- Many-to-Many: A user can attend multiple events, and an event can have many attendees.

- User:
 - One-to-Many: A single user can create multiple events.
 - One-to-Many: A single user can comment on multiple events.
 - Many-to-Many: A user can attend multiple events, and events can have multiple attendees.


![ER Diagram](static/readme-img/erd/ERD.png)

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

<details><summary><b>T-shirt size Story Points</b></summary>

![Story Points Estimation](static/readme-img/Agile/T-shirt-size-story-points.webp)

</details>

<br>

# UI Design

The initial wireframe was designed using figma. The figma project page can be found here [FIGMA THE WORD](https://www.figma.com/design/xioX2poOx76Zg7R8lG8Ret/The-Word!-Events?node-id=218-1347&node-type=frame&t=6gK5eYLXELZdjBK1-0)

## Wireframes

#### Mobile Wireframe

![mobile wireframe](static/readme-img/UX/mobile-wireframe.png)

#### Desktop Wireframe

![Desktop wireframe](static/readme-img/UX/Desktop-wireframe.png)

### Design Style

The UI design for the app was to be a modern, clean and userfriendly. Balancing functionality and aesthetics, so the user can easily navigate through the app.

#### Colour Palette:
- Primary background colour of dark blue #1B4965. 
  - Giving a strong rich coloured canvas for the event cards. By doing this the cards stand out and draws the users eye inward.
- Accent Colours: Orange and teal-green for the action buttons.
  - It balances well with the darker and neutral colors of the site, maintaining a professional tone while being inviting.
- Neutral Colors: light & slate greys. 
  - Not distracting or overpowering. They are in keeping with the design and are easily read.
- White
  - Background colour of the cards, making them pop from the background.

<hr>

![Colour Palette](static/readme-img/UX/colours.png)

#### Typography:
- Font Bondoni Moda SC, Serif
  - The choice of a serif over a more modern font was a not to the past, or an acknowledgment of Djangos start. The idea that news was initally printed in serif.


### Interaction

#### Buttons and Icons

The action buttons like signup, edit, delete and next/previus are solid colours when inactive and white with colour text and border when hovered over.
This was due to the type of button is was. Once clicked they were gone. 
- The icon buttons fo the categories and attending buttons are differnt however. 
  - The categories are on a white bar and would be distracting if they were block colours initially. Once a category is active it colour needs to inform the user of their location with a obvious sign. A quote from Steve Krug from his book "don't make me think" 
    - “The fact that the people who built the site didn’t care enough to make things obvious—and easy—can erode our confidence in the site and the organization behind it.”

- The icons are from [fontawesome](https://fontawesome.com/)
<hr>

![Category buttons](static/readme-img/UX/category-button.png)


![Action button with edit:hover](static/readme-img/UX/edit-button-hover.png)


### Design familiarity
  - Attending button: Just like the categories buttons, this had to be obvious. There is many apps with this idea of liking or attening. This grey to green concept is intuitive. This leverages the users prior experiences, making it feel familiar and natural.
  <hr>

![Attending Button](static/readme-img/UX/attending-icon.png)


#### Cards

- In keeping with the dark background the cards are white to standout, indicating importance. 
- The card displays an image with text under it. There is a Learn more link element that is a "signifier" to click to view more information. 
- I have made the whole card a link even though it looks like the blue "Learn more" is the link. This was done to make it easier for the user to move to the next page. All designed with the user in mind. 
- There is a slight drop shadow on the cards as well.

#### Navbar.

- The Navbar contains 6 links when the user is not signed in and 5 links when they are
  - All Events
  - Calander
  - Create an event
  - My events
  - Register, This button is not visable when logged in
  - Login / login changes to logout when the user is logged in

- This is a Bootstap NavBar that has it's own JavaScript for the hamburger menu on smaller devices.

- The links are grey when not active and black when active. The user will always know where they are on the app.
- I decided to keep the categories section seperate to the navbar for a more asthetic design. This design is familiar to other event sites, making it intuitive.


### User Interaction with messages

- Messages: Bootstrap alerts are used to notify users of actions like logging in or creating an event. These are styled with transparent color overlays to blend smoothly into the page without overwhelming the user.
- Authentication Indicators: Users are reminded whether they are logged in or not through a simple text message, presented in a “log-box” style, centered on the page in grey. 

### Footer:

- Dark-Grey Background with white text ensures that the footer remains subtle but clear. It contains social media links, styled with white icons against the dark background, providing easy access to external community pages without dominating the visual hierarchy. User are used to having these external links on the footer.

![Footer](static/readme-img/UX/Footer.png)


### Bootstrap

Bootstrap was used in the app to create a responsive, mobile-first websites quickly and efficiently using it's libarary. Bootstrap provides a collection of pre-designed HTML, CSS, and JavaScript components, like buttons, forms, navigation bars, and grid layouts. By using Bootstrap, I was able to build a visually consistent app without writing extensive custom code. It was easy to customise and it adapted to all screen sizes without having to write additional media queries. Saying this, I did customise the css and added js in this build.





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

### Languages
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website


### Frameworks & Software
- [Gitpod](http://gitpod.io) - Cloud based IDE
- [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
- [Django](https://www.djangoproject.com/) 
- [Figma](https://www.figma.com/) was used to create the final design of a website.
- [Github](https://github.com/) - Used to host and edit the website.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
- [Font Awesome](https://fontawesome.com/) was used for social media icons in the footer.
- [Favicon](https://favicon.io/) was used for favicon.
- [LucidChart](https://lucid.co/) was used for creating ERD.
- [Google Fonts](https://fonts.google.com/) was used to add specific font family to the stylesheet.
- [W3C validation](https://validator.w3.org/) was used to check the markup validity of html file.
- [Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the validity of css file.
- [JSHint](https://jshint.com/) was used to check the validity of js files.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.
- [Am I Responsive](https://ui.dev/amiresponsive) was used to get a screenshot of a final look of the website on various devices.
- [Github](https://github.com/) was used to store the code of the website.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [Cloudinary](https://cloudinary.com) used for images
- [Gunicorn](https://gunicorn.org/) used for WSGI server
- Photoshop: Resizing and editing pictures


### Create a PostgreSQL Code Institute database

- Log into [CIdatabase maker](https://dbs.ci-dbs.net/)
- Add your email address in input field and submit the form
- Open database link in your email
- Paste dabase URL in your DATABASE_URL variable in env.py file and in Heroku config vars

### Cloudinary

- Navigate to https://cloudinary.com/ and log in to your account.
- Navigate to dashboard/console https://console.cloudinary.com/console/  copy API Enviroment variable starting with "cloudinary://".
- Paste copied url CLOUDINARY_URL variable in env.py file and in Heroku config vars
- Update settings.py

### Django secret key

You need to include you Django secret key that you can generate using any of the Django secret keys generators online.
In order to protect django app secret key it was set as an enviroment variable and stored in env.py.

```
os.environ.setdefault(
    "SECRET_KEY", "your secret key")
```

## Deployment

### Heroku Deployment
This site was deployed to and is currently [hosted on the Heroku platform](https://astroshare-blog-6a7ca9d34749.herokuapp.com/). The steps for deploying to Heroku, using PostgreSQL as the database host, are as follows:

1. Create a list of requirements in the requirements.txt file by using the command pip3 freeze > requirements.txt
2. Log in (or sign up) to Heroku
3. Click on the New button and select *Create new app*
4. Give it a unique name and choose the region *Europe*
5. Click the Settings tab, go to the *Config Vars* section and click on the Reveal Config Vars button
6. Add all variables from *env.py* to ConfigVars of Heroku

<details><summary><b>Click to view details Config Vars Heroku</b></summary>

![Config vars](static/readme-img/code/Config-Vars.png)
</details>

7. Click the *Add* button
8. Click the *Deploy* tab, go to the *Deployment method section*, select *GitHub* and confirm this selection by clicking on the *Connect to Github* button
9. Search for the repository name on github *Astro Blog* and click the *Connect* button
10. Add in the *setting.py* the Heroku app URL into ALLOWED HOSTS
11. Gather all static files of the project by using the command *python3 manage.py collectstatic* in the terminal
12. Make sure that DEBUG=FALSE in *settings.py*
13. Create a *Procfile* in the root directory and add *web: gunicorn astroshare-blog.wsgi*
14. In Heroku enable the automatic deploy or manually deploy the code from the main branch

### Local Deployment
1. Generate an *env.py* file in the root directory of the project
2. Configure the environment variables within this file
3. Create a virtual environment
4. Install all required dependencies using pip install command into the .venv
5. Add dependencies to the requirements.txt file using pip3 freeze > requirements.txt command

### Final Deployment

1. Make sure to set DEBUG = False.


### Validator Testing 


### HTML

All pages have been passed through the W3C validator. The only page that had an error was the the sign-up page
Django Summernote issue: It's a known bug that adds extra paragraph tags to the body content in the posts.
I’m aware of the issue/bug coming from Django Summernote.

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

No CSS issues

[Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check css files

<details><summary><b>style.css</b></summary>

![Logout page](static/readme-img/code-validated/css.png)

</details>

### JavaScript

[Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check css files

Calendar.js 
- When testing the calendar js an error of undefined variable FullCalendar. FullCalendar is a django library. new FullCalendar.Calendar is called to create a new calendar instance,in the html id=calander.

eventsComments.js
- When testing the eventComments js an error of undefined variable Bootstrap. Bootstrap is a Django library. new Bootstrap.Modal creates a modal instance and provides the functionality to interact with that modal.


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

#### PIP8 Compliant

| File                   | Result |
|------------------------|--------|
| settings.py            | Pass AUTH_PASSWORD_VALIDATORS line too long|
| urls.py                | Pass   |
| admin.py               | Pass   |
| manage.py              | Pass   |
| apps.py                | Pass   |
| forms.py               | Pass|
| models.py              | Pass   |
| Project urls.py        | Pass   |
| wsgi.py                | Pass   |
| asgi.py                | Pass   |
| Models.py              | Pass   |

The 4 lines in setting.py that are too long is the AUTH_PASSWORD_VALIDATORS. There are automatically generated and can be left. All other python files passed.
<details><summary><b>Settings.py CI Linter result</b></summary>

![Settings.py CI Linter](static/readme-img/code-validated/settings.py-ci-linter.png)

</details>

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.
