from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from tasks.serializers import TaskSerializer
from tasks.models import Task

class TaskAPI(GenericViewSet,
            mixins.UpdateModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.ListModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer