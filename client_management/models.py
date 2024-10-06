from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='assigned_projects')  # Use a custom related name
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')  # Another custom related name
