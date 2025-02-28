from django.urls import path
from .views import *

urlpatterns = [
    # POST - Create a new job listing
    path('jobs/create/', JobCreateView.as_view(), name='job-create'),
    
    # GET - Retrieve a list of all job listings
    path('jobs/', JobListView.as_view(), name='job-list'),
    
    # GET - Retrieve jobs that match a specific number of years of experience
    path('jobs/experience/<int:experience>/', JobByExperienceView.as_view(), name='job-by-experience'),
    
    # GET - Group jobs by years of experience with count
    path('jobs/group-by-experience/', JobGroupByExperienceView.as_view(), name='job-group-by-experience'),
]
