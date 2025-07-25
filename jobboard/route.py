from .views import JobViewSet,ApplicationViewset,CompanyViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.