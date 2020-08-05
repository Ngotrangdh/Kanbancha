from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Project, Task, Comment
from users.models import Profile
from .forms import ProjectForm, TaskForm


@login_required
def index(request):
    projects = request.user.project.all()
    context = {"projects": projects, "profiles": Profile.objects.all()}
    return render(request, "tasks/index.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.pm = request.user
            project.save()
            project_name = project.title
            project_form.save_m2m()
            messages.success(request, f"Project {project_name} has been created")
            return redirect("project", project_id=project.id)
    else:
        project_form = ProjectForm()

    return render(request, "tasks/new-project.html", {"project_form": project_form})


@login_required
def update_project(request, project_id):
    project_instance = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project_form = ProjectForm(request.POST, instance=project_instance)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.save()
            project_form.save_m2m()
            messages.success(request, f"Project {project.title} has been updated")
            return redirect("project", project_id=project_id)
    else:
        project_form = ProjectForm(instance=project_instance)

    context = {"project_form": project_form, "project_id": project_id}

    return render(request, "tasks/update-project.html", context)


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()

    return redirect("index")


@login_required
def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    todos = Task.objects.filter(project=project, status="T")
    in_progress = Task.objects.filter(project=project, status="P")
    done = Task.objects.filter(project=project, status="D")

    context = {
        "project": project,
        "todos": todos,
        "in_progress": in_progress,
        "done": done,
    }
    return render(request, "tasks/project.html", context)


@login_required
def create_task(request):
    assignor = request.user
    title = request.POST.get("title")
    status = request.POST.get("status")
    project_id = int(request.POST.get("project_id"))
    task = Task.objects.create(
        title=title,
        project=Project.objects.get(pk=project_id),
        status=status,
        assignor=assignor,
    )

    return HttpResponse(status=201)


@login_required
def update_task_status(request):
    status = request.POST.get("status")
    task_id = int(request.POST.get("task_id"))
    updated_task = get_object_or_404(Task, pk=task_id)
    updated_task.status = status
    updated_task.save()

    return HttpResponse(status=201)


@login_required
def update_task(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    comments = task_instance.comment_set.all()
    project = task_instance.project
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task_instance)
        if task_form.is_valid():
            task_form.save()
            return redirect("project", project_id=task_instance.project.id)
    else:
        task_form = TaskForm(instance=task_instance)

    context = {
        "task_form": task_form,
        "comments": comments,
        "task_id": task_id,
        "project": project,
    }

    return render(request, "tasks/update-task.html", context)


@login_required
def delete_task(request):
    task_id = int(request.POST.get("task_id"))
    task = get_object_or_404(Task, pk=task_id)
    task.delete()

    return HttpResponse(status=201)


@login_required
def create_comment(request):
    task_id = int(request.POST.get("task_id"))
    task = Task.objects.get(pk=task_id)
    comment = Comment.objects.create(
        commenter=request.user, content=request.POST.get("content"), task=task
    )

    return HttpResponse(status=201)


@login_required
def my_tasks(request):
    tasks = request.user.assignee.all()
    return render(request, "tasks/my-tasks.html", {"tasks": tasks})
