from django import forms
from django.contrib.auth.models import User

from .models import Project, Task, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'manager', 'members', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'members': forms.CheckboxSelectMultiple(),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name',
                  'description',
                  'assignee',
                  'priority', 'status', 'start_date', 'end_date',
                  # 'deadline_date',
                  ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            # 'deadline_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if project:
            # self.fields['project'].queryset = Project.objects.filter(members=user)
            self.fields['assignee'].queryset = User.objects.filter(projects=project.id)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
