from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
from .models import Job
from .serializers import JobSerializer


# Create a new job
class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# List all jobs
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Fetch jobs by experience
class JobByExperienceView(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        experience = self.kwargs.get('experience')
        return Job.objects.filter(experience=experience)

# Group jobs by experience
class JobGroupByExperienceView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        grouped_jobs = Job.objects.values('experience').annotate(count=Count('id'))
        return Response(grouped_jobs)
