from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, Comment
from .forms import ProjectForm, TaskForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('projects_list')
    else:
        form = UserCreationForm()
    return render(request, 'projectman/registration.html', {"form": form})


@login_required(login_url='/login/')
def projects_list(request):
    projects = Project.objects.filter(members=request.user)
    return render(request, 'projectman/projects_list.html', {"projects": projects})


@login_required(login_url='/login/')
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.members.add(request.user)
            return redirect('projects_list')
    else:
        form = ProjectForm()
    return render(request, 'projectman/project_form.html', {"form": form})
