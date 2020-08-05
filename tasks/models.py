from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    pm = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pm")
    members = models.ManyToManyField(User, related_name="project")

    def __str__(self):
        return f"{self.title}"


class Task(models.Model):
    TODO = "T"
    PROGRESS = "P"
    DONE = "D"
    STATUS_CHOICES = [
        (TODO, "Todo"),
        (PROGRESS, "Progress"),
        (DONE, "Done"),
    ]

    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignee", null=True, blank=True,
    )
    assignor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignor"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
