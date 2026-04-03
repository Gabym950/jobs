from rest_framework import viewsets
from rest_framework.response import Response

from .models import Job
from .serializers import JobSerializer


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ["get", "post", "head", "patch", "delete"]

    def get_queryset(self):
        queryset = Job.objects.filter(status="OPEN")
        query = self.request.query_params.get("q", None).strip()
        if query:
            queryset = queryset.filter(title__icontains=query)  
        return queryset
