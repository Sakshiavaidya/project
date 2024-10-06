from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects']
