from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def add_project(self, request, pk=None):
        client = self.get_object()
        project_name = request.data.get('project_name')
        user_ids = request.data.get('users')

        users = User.objects.filter(id__in=user_ids)
        project = Project.objects.create(project_name=project_name, client=client, created_by=self.request.user)
        project.users.set(users)
        project.save()

        return Response(ProjectSerializer(project).data)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)
