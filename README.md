# Final project - Kanban

A Project Management Web Application built upon Django and javascript

## Features

Allow users to:

-   Register, login, logout and edit their profile (username, email, profile picture)

-   Create projects
-   Add members to a project
-   Update a project details
-   Delete projects

-   Add tasks to a project
-   Set deadline for tasks
-   Assign tasks to one of the members in the project
-   Update a task details
-   Delete tasks

-   Post comments within task view

## tasks app

### tasks/models.py

Specify three models:

-   Project: defines a project, which has title, description, created date, pm (project manager - who creates the project) and members
-   Task: defines a task, which has title, project (it belongs to), description, assignee, status (to do, in progress, done) and due_date
-   Comment: defines a comment, which has commenter (author), content, task (it belongs to) and created_date

### tasks/view.py + orders/templates/orders

#### index()

-   Render index.html which lists all the projects that the user belongs to

#### create_project()

-   Render new-project.html which contains a project_form allowing users to create a new project

#### update_project()

-   Render update-project.html which contains a project_form allowing users to update the project details

#### delete_project()

-   Handle a delete post request and redirect user to the index page

#### tasks()

-   Render tasks.html which lists all of the tasks of a choosen project and its details

#### create_task()

-   Handle post ajax requests from client side to create new tasks

#### update_task_status()

-   Handle post ajax requests from client side to update tasks' status

#### update_task()

-   Render update-project.html which contain a task_form allowing users to update the task details

#### delete_task()

-   Handle post ajax requests from client side to delete tasks

#### create_comment()

-   Handle post ajax requests from client side to create new comments

#### my_tasks()

-   Render my-tasks.html which lists all of the tasks (might be from different projects) that were assigned to the user

### tasks/static/tasks/main.js

-   Get Csrf token to submit along with every post ajax request
-   Specify an empty card to add a new task
-   Create an empty card to add a new task
-   Post the new added task to server by calling function postNewTask()
-   Update task status by calling function updateTaskStatus()
-   Delete task by calling function deleteTask()
-   Post comment by calling function postNewComment()
-   Specify function postNewTask()
-   Specify function updateTaskStatus()
-   Specify function deleteTask()
-   Specify function postNewComment()

## users app

Handle the user registration and authentication

-   I take advantage of the LoginView and LogoutView class from django.contrib.auth to log in and logout users.
-   In users/forms.py, I add an email field to the built-in UserCreationForm in Django, so the SignupForm now has four fields: username, email, password1, password2
-   In users/models.py, I specify a class (Profile) to represent each user's profile and override its default save() function to save the user's profile picture as with a desired size
-   In users/signals.py, I use the post_save built-in signal to trigger the save_profile() function to create and save profile when a User instance finalize the execution of its save method
-   The urls for login, logout, register views are specified in project-level urls.py

## Additional packages

-   django-bootstrap-datepicker-plus
-   django-bootstrap4
-   django-crispy-forms
-   Pillow
