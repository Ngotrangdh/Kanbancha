from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newproject", views.create_project, name="new-project"),
    path("updateproject/<int:project_id>", views.update_project, name="update-project"),
    path("updatetask/<int:task_id>", views.update_task, name="update-task"),
    path(
        "delete-project/<int:project_id>", views.delete_project, name="delete-project"
    ),
    path("project/<int:project_id>", views.project, name="project"),
    path("tasks", views.my_tasks, name="my-tasks"),
    path("project/api/create-tasks/", views.create_task, name="create-task"),
    path("updatetask/api/create-comment/", views.create_comment, name="create-comment"),
    path(
        "project/api/update-task-status/",
        views.update_task_status,
        name="update-task-status",
    ),
    path("project/api/delete-task/", views.delete_task, name="delete-task"),
]
