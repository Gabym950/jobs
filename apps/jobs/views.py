from rest_framework import viewsets
from rest_framework.response import Response

from .models import Job
from .serializer import JobSerializer


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ["get", "post", "head", "patch", "delete"]

    def search(self, request):
        query = request.query_params.get("q", "")
        jobs = Job.objects.filter(title__icontains=query)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
