from django.contrib import admin
from django.utils.html import format_html_join
from .models import Project, Task, Comment


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    readonly_fields = (
        "title",
        "description",
        "assignor",
        "assignee",
        "created_date",
        "due_date",
        "comments",
    )

    def comments(self, instance):
        if len(list(Comment.objects.filter(task=instance))) != 0:
            return format_html_join(
                "\n",
                "<li>{}</li>",
                (
                    comment.content
                    for comment in list(Comment.objects.filter(task=instance))
                ),
            )
        else:
            return "No comments"


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task)
admin.site.register(Comment)
