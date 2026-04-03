from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Job
from .serializers import JobSerializer


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (
        filters.DjangoFilterBackend,
    )
    filterset_fields = ("status",)
    http_method_names = ["get", "post", "head", "patch", "delete"]

    def get_queryset(self):
        queryset = Job.objects.filter(status="OPEN")
        query = self.request.query_params.get("q", "").strip()
        if query:
            queryset = queryset.filter(title__icontains=query)  
        return queryset
