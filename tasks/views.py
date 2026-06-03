import datetime

from rest_framework import viewsets

from .models import Task, SubTask, Comment
from .serializers import TaskSerializer, SubTaskSerializer, CommentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        unused_var = "test"
        return super().list(request, *args, **kwargs)

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer