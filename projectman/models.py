from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.ForeignKey(User, related_name='managed_projects', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
        ('U', 'Urgent'),
    ]
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('D', 'Done'),
    ]
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    assignee = models.ForeignKey(User, related_name='tasks', on_delete=models.PROTECT, null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    # deadline_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.task}'
