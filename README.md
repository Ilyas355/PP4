# Productivity App

This website was created for my 4th Portfolio Project with Code Institute. Productivity App is multifacited app with mutliple features including a chat app and a task management system for both site users and site admins (called external users). The purpose behind this app is to provide users in companies or even education centers a platform to manage daily tasks and effectively communicate with each other seemlessly.
<br>
Live link to the deployed app on heroku - [Productivity App](https://productivity-app-pp4-6c2bd8f4331e.herokuapp.com)
<br>

## Table of Contents

- [User Experience Design](#user-experience-design)
- [Strategy](#strategy)
  - [User Stories](#user-stories)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
  - [Wireframes](#wireframes)
- [Surface](#surface)

### Features

- [Existing Features](#existing-features)
- [CRUD (Create, Read, Update, Delete)](#crud-create-read-update-delete)
- [Future Features](#future-features)

### Technology

- [Languages Used](#languages-used)
- [Libraries and Programs Used](#libraries-and-programs-used)

### Testing

- [Automated Testing](#automated-testing)
- [Manual Test Cases](#manual-test-cases)
- [Code Validation](#code-validation)
- [Lighthouse Performance Testing](#lighthouse-performance-testing)
- [Debugging](#debugging)
- [Unfixed Bugs](#unfixed-bugs)
- [Testing on Different Browsers and Screen Sizes](#testing-on-different-browsers-and-screen-sizes)

### Deployment

- [Deployment Process](#deployment-process)

### Credits

- [Resources Used](#resources-used)
- [Content Contributors](#content-contributors)
- [Honourable Mentions](#honourable-mentions)

---

## User Experience Design

## Strategy

### __Typical Users__
  
  - A typical Site User would be an employee in a companee or student in a school who needs to have the daily tasks supervised and managed.

  - The Site Admin would be a manager in a company or a teacher in a school that supervises the tasks or regular users.


### User Stories

#### Site User

  - Account Register: I can sign up or log in to an account so that I can access all chat and task management features.

  - Edit Profile: I can edit my personal profile to have my own user image and decide what information is displayed.

  - Send Message (Public Channel): I can send a message in a public channel so that I can participate in group discussions.

  - Send Message (Private Channel): I can send a direct message to another user or a group so that I can have private conversations.

  - View Chat History: I can view past messages in a public or private channel so that I can keep track of previous conversations.

  - Edit Message: I can edit my own messages so that I can correct mistakes or update information.

  - Delete Message: I can delete my own messages so that I can remove unwanted or incorrect messages.

  - Manage Tasks: I can create, read, update, and delete my own tasks so that I can keep track of my work.

  - View Task Details: I can view the details of my tasks so that I can understand deadlines, descriptions, and progress.

  - Complete Task: I can mark a task as complete so that I can track progress and know what has been finished.

  - Filter and Sort Tasks: I can filter and sort my tasks by priority, deadline, or status so that I can focus on important tasks.

<br>

#### Superuser (Admin)

  - Manage Public Channels: I can create, edit, and delete public channels so that I can structure discussions properly.

  - Delete Message: I can delete any message in public and private chats so that I can ensure a respectful and safe environment.

  - Manage Tasks (All Users): I can create, update, and delete tasks for any user so that I can oversee task management.

  - View All Tasks: I can view all tasks assigned to users so that I can monitor work progress.

<br>

## Scope

<br>

An MVP (Minimum Viable Product) approach was taken to the development of this site. The main features deemed as basic requirements for this site were:

- Account Registration
- CRUD Functionality (Both for Site User and Site Admin)
- Device Responsiveness

 For a more detailed explanation of all existing features see [Existing Features](#existing-features). [Future Features](#future-features) were still within the possible scope of this project, they were not necessary at this point in time for the site to still work.

## Structure

### Site Navigation Flowchart

  The Flow chart was made to see the structure of navigation on the page. The flowchart was created with [Lucid](https://lucid.app/documents#/dashboard).

  ![Flowchart](docs/readme_images/site-navigation.png)

## Skeleton

### Wireframes

<br>

<details>
  <summary>Chat page wireframes</summary>

  ![chat search page](docs/wireframes/chat_search_page.jpg)
  <br>

  ![chat general server](docs/wireframes/chat_public_server.jpg)
  <br>

  ![chat announcements server](docs/wireframes/chat_public_server_2.jpg)
  <br>
  
  ![chat private server](docs/wireframes/chat_private_server.jpg)

</details>
<br>
<br>
  

<details>
  <summary>Tasks wireframes</summary>

  ![tasks](docs/wireframes/tasks.jpg)

  </details>
<br>
<br>

<details>
  <summary>External tasks wireframes</summary>

  ![external tasks search](docs/wireframes/external_tasks_search.jpg)
  <br>

  ![external tasks page](docs/wireframes/external_tasks_page.jpg)

</details>
<br>

<br>

<details>
  <summary>Profile wireframes</summary>

  ![profile](docs/wireframes/profile_page.jpg)
  <br>

  ![profile](docs/wireframes/logged_out_page.jpg)
  <br>

</details>
<br>

### Database design


- Below is a relational diagram for the design of the database in this project.

<br>

![database design](docs/readme_images/database-screenshot.png)


## Surface

- ## Colour-Scheme

  - The main color schemes for the website are Dark Gray ( #2d2f31, Top Navbar Background) and White (#ffffff, Main Background). Light Blue, Green and Red for links, notifications and buttons and Dark Gray/Black for Text.

- ## Typography

  - The Segoe UI font was used throughout the website.


- ## Agile Methodology

    An Agile approach was taken for the management of this project.

    - User stories were written for each of the site's features.

    - The user stories were then managed in a Kanban board, which was created in GitHub Projects.

## Features

### __Existing Features__

### Login Page
- This page is where users with existing accounts log in to the app

<br>

![Login Page](docs/readme_images/login-page.png)

<br>

### Logout Page
- This page lets users know they've been logged out and gives them the option to log back in.

<br>

![logout Page](docs/readme_images/logged-out-page.png)

<br>

### Sign Up Page
- This page is where users have the option to create new accounts.

<br>

![Sign Up Page](docs/readme_images/sign-up-page.png)

<br>

### Chat Room Search Page
- Here users can either select one of the public rooms available or enter a private room of their choice to communicate through. 

<br>

![Chat Home Page](docs/readme_images/chat-home.png)

<br>

### Chat Room Page
- Here users can communicate with one another by sending messages through the different rooms.
- Users are able edit and delete their own messages but not the messages of others.

<br>

![Chat Room Page](docs/readme_images/chat-room.png)

<br>

### Tasks Page
- The tasks page is where users are able to manage their own tasks by:
  - view their tasks
  - filter their tasks
  - adding new tasks
  - deleting tasks
  - editing the content of tasks
  - editing the status of tasks

<br>

![Tasks Page](docs/readme_images/tasks-tab.jpg)

<br>

### User Search Page
- Here site admins can search for users and proceed to manage their tasks.

<br>

![External Tasks Search Page](docs/readme_images/external-tasks-search.png)

<br>

### External Tasks Page
- Here site admins can manage the tasks of other users.

<br>

![External Tasks Page](docs/readme_images/external-tasks-user.png)

<br>

### Profile Page
- Here users are able to update their account details as shown in the image.

<br>

![Profile Page](docs/readme_images/profile-page.png)

<br>

---

### CRUD (Create, Read, Update, Delete)

#### __Site User__

#### Create:

- Can create an account by registering.

- Can create and update their profile (upload image, set info).

- Can send messages in public and private channels.

- Can create tasks for themselves.

#### Read:

- Can view public and private chat history through the channel groups.

- Can read all of their tasks and associated details (description, status).

- Can view their own profile and those of users they interact with.

#### Update:

- Can edit their profile.

- Can edit their own messages.

- Can update their own tasks (description, status).

- Can filter/sort their tasks for better organization.

- Can mark tasks as complete.

- Can mark tasks incomplete

#### Delete:

- Can delete their own messages.

- Can delete their own tasks.

<br>

---

#### __Site Admin__

#### Create:

- Can create public/private channels.

- Can create tasks for any user.

#### Read:

- Can read all chat messages and all tasks, regardless of user.

#### Update:

- Can update public channels, tasks for any user, and user accounts.

#### Delete:

- Can delete any task.

- Can delete user accounts if needed.

- Can delete public channels if inappropriate or outdated.

<br>

---

### __Future Features__

#### Features to implement in the future would include:

- reacting to messages

- commenting on messages

- site admins being able to assign tasks to multiple users

- adding deadlines to tasks



## Technology

- ### Languages Used

     - HTML
     - CSS
     - JavaScript
     - Python
     - Django
     - Unitest (Django’s unit tests)


- ### Libraries and Programs Used

    - Git - Was used for version control, the Gitpod terminal to commit and push to GitHub.

    - [GitHub](https://github.com/) - Was used to store the project code and display the project in GitHub Pages.

    - [Balsamiq](https://www.Balsamiq.com/) - Was used to create the wireframes.

    - [Lucid](https://lucid.app/) - Was used to create the flowcharts.

    - Google Dev Tools- Were used to test and troubleshoot the webpage as well as fix problems with responsive design and styling.

    - [Favicon](https://favicon.io/) - Was used to take the logo and make it into a favicon.

    - [Heroku](heroku.com) - Where used for Deployment.

    - [Bootstrap](https://getbootstrap.com/) - Where used for CSS and some HTML.

    - [PostgreSQL](https://www.postgresql.org/) - Was used for PostgreSQL database hosting.

    - [Cloudinary](https://console.cloudinary.com/) - Where used to save static media files.

---

## Testing

### Automated Testing

The automated testing was completed using Django’s unit tests Python standard library module Unittest for the Django files: "models.py", "urls.py", and "views.py" in my chat app and tasks app. This tested the core functionalities of the application with the remaining tests handled in the manual test cases.

![automated-tests](docs/testing/automated-tests.png)


## Manual Test Cases

####  General Users

**1. Users are able to sign up and create an account**  
- Navigate to the "Sign Up" link in the navigation bar.  
- Fill out the registration form with a username, email, and password.  
- Submit the form.  
- ✅ **Expected result**: User is redirected to the home/dashboard page and receives a success message.

**2. Users are able to log in to their accounts**  
- Navigate to the "Log In" link in the navigation bar.  
- Enter valid login credentials (username and password).  
- Submit the form.  
- ✅ **Expected result**: User is logged in and redirected to their task dashboard with a welcome message.

**3. Users are able to log out of their accounts**  
- While logged in, click the "Logout" link in the navigation bar.  
- ✅ **Expected result**: User is logged out and redirected to the login page or home page with a logout confirmation.

**4. Users are able to update their profile info**  
- Navigate to the "Edit Profile" or "Profile Settings" from the navbar or profile dropdown.  
- Update fields such as name, email, bio, or profile picture.  
- Submit the form.  
- ✅ **Expected result**: Changes are saved and reflected on the profile page. A success message is shown.

---

####  Admin Users

**1. Admin is able to view tasks for any user**  
- Log in as a superuser.  
- Go to the admin tasks page or use the external task viewer.  
- Enter a valid username to view their tasks.  
- ✅ **Expected result**: A list of the selected user's tasks is displayed with correct filter options (all, week, month, etc.).

**2. Admin is able to create a task for any user**  
- On the admin/external tasks page, enter a valid username and task content.  
- Submit the form.  
- ✅ **Expected result**: The task appears in the user's task list and shows correct creation date and status.

**3. Admin is able to edit any user's task**  
- Click on a task to expand the form.  
- Modify task content or completion status.  
- Submit the update.  
- ✅ **Expected result**: The task is updated and the changes are visible immediately.

**4. Admin is able to delete any user's task**  
- From the admin task list, click the delete icon/button next to a task.  
- Confirm deletion if applicable.  
- ✅ **Expected result**: Task is removed from the list and a success message may be shown.

---

## Code Validation
### HTML
- All html code in my code were put through html code validator and all errors where fixed.

![html](docs/testing/html-validation.png)

### CSS
- All css code in my code were put through css code validator and all errors where fixed.

![css](docs/testing/css-validation.png)

### JS
- All my javascript scripts were put through the JS Hint and no errors were returned.

![JS Validation](docs/testing/JS-Hint-validation.png)


### Python
- All my Python files were put through the CI Python Linter and no errors were returned.

![Python Validation](docs/testing/CI-Python-Linter-Validation.png)

## Lighthouse Performance Testing

   - All pages achieved a great score for accessibility performance.

![lighthouse testing](docs/testing/productivity-app-accessibility.png)

## Unfixed Bugs

Due to time contstraints I wasn't able to address and fix the following bugs in my project:
- When messages are deleted in the chatrooms or are edited users are forced to be redirected to the home page due to a deficient implementation of my delete messages function.
- When a site admin deletes the tasks of other users they are redirected to their tasks page do to a limited implementation of my delete tasks function.

## Testing on Different Browsers and Screen Sizes

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [productivity app](https://productivity-app-pp4-6c2bd8f4331e.herokuapp.com)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
-  Click and drag the responsive window to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen

## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘PP4’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [productivity app](https://productivity-app-pp4-6c2bd8f4331e.herokuapp.com)

## Credits

- My favicon image was created using this websiste [promeai.pro](https://www.promeai.pro/).
- At different parts of the project text was generated using chatgpt.
- I used websites like stack overflow frequently when debugging throughout the project.
- Some of the basic structure of my chat app (and login/sign in and profile system) was inspired and modelled by existing django chat apps like [Django Chat App](https://github.com/rustyxlol/Django-ChatApp) and tutorials as mentioned in the resources section.

### Resources Used

- [Django Channels - RealPython](https://realpython.com/getting-started-with-django-channels/)
- [Django Channels](https://channels.readthedocs.io/)
- [Django Channels and WebSockets oversimplified - Dennis Ivy](https://www.youtube.com/watch?v=cw8-KFVXpTE)