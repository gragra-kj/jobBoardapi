from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .serializer import ApplicationSerializer,JobSerializer,CompanySerializer
from .models import ApplicationModel,JobModel,CompanyProfile
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

#register

@api_view(['POST'])
def register_user(request):
    username=request.data.get('username')
    password=request.data.get('password')
    
    if username is None or password is None:
        return Response({'error':'Please enter both password and username'},status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error':'username already exists'},status=status.HTTP_400_BAD_REQUEST)
    
    
    user=User.objects.create_user(username=username,password=password)
    token=Token.objects.create(user=user)
    
    return Response({'token':token.key},status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    username=request.data.get('username')
    password=request.data.get('password')
    
    user=authenticate(username=username,password=password)
    if not user:
        return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
    
    token,created=Token.objects.get_or_create(user=user)
    return Response({'token':token.key})

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
