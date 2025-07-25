from .views import JobViewSet,ApplicationViewset,CompanyViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('jobs',JobViewSet)
router.register('application',ApplicationViewset)
router.register('company',CompanyViewSet)

urlpatterns=[
    path('',include(router.urls))
]