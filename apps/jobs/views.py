from rest_framework import viewsets
from rest_framework.response import Response

from .models import Job
from .serializer import JobSerializer


class JobView(viewsets.ViewSet):
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def retrieve(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        serializer = JobSerializer(job)
        return Response(serializer.data)

    def list(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def search(self, request):
        query = request.query_params.get('q', '')
        jobs = Job.objects.filter(title__icontains=query)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        serializer = JobSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        job.delete()
        return Response(status=204)
