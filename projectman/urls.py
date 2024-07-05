from django.urls import path
from .views import *

urlpatterns = [
    path('', projects_list, name='projects_list'),
    path('registration/', registration, name='registration'),
    path('project_form/', project_create, name='project_create'),
]
