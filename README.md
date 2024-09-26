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


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Andrew O'Dwyer,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
