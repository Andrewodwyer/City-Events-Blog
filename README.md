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


For Organizers: 
- Users who create events are looking for an easy way to promote their events, manage their listings, and interact with potential attendees. The platform’s CRUD (Create, Read, Update, Delete) functionality provides them with the flexibility to create, edit, or remove events as needed. Giving them full control over their event.


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