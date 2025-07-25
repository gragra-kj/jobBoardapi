from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .serializer import ApplicationSerializer,JobSerializer,CompanySerializer
from .models import ApplicationModel,JobModel,CompanyProfile

class ApplicationViewset(viewsets.ModelViewSet):
    #queryset=ApplicationModel.objects.all()
    serializer_class=ApplicationSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        return ApplicationModel.objects.filter(applicant=self.request.user)
    
class JobViewSet(viewsets.ModelViewSet):
    #queryset=JobModel.objects.all()
    serializer_class=JobSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return JobModel.objects.filter(posted_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
    
class CompanyViewSet(viewsets.ModelViewSet):
    #queryset=CompanyProfile.objects.all()
    serializer_class=CompanySerializer
    permission_classes=[permissions.IsAuthenticated] 
    
    def get_queryset(self):
        return CompanyProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)       
