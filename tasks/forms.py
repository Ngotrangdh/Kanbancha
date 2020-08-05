from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from django.contrib.auth.models import User
from .models import Project, Task, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "members"]
        widgets = {
            "members": forms.SelectMultiple(
                attrs={
                    "class": "js-example-basic-multiple",
                    "name": "members[]",
                    "multiple": "multiple",
                }
            ),
        }


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if instance:
            self.fields["assignee"].queryset = User.objects.filter(
                project=instance.project
            )

    class Meta:
        model = Task
        fields = ["title", "assignee", "due_date", "project", "status", "description"]
        widgets = {
            "assignee": forms.Select(
                attrs={"class": "js-example-basic-single", "name": "assignee",}
            ),
            "due_date": DateTimePickerInput(),
            "description": forms.Textarea(attrs={"cols": 80, "rows": 2}),
            "project": forms.HiddenInput(),
        }
