from .views import JobViewSet,ApplicationViewset,CompanyViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter
#from rest_framework.documentation import include_docs_urls


router=DefaultRouter()

router.register('jobs',JobViewSet,basename='job')
router.register('application',ApplicationViewset,basename='application')
router.register('company',CompanyViewSet,basename='company')

urlpatterns=[
    path('',include(router.urls)),
    #path('docs/', include_docs_urls(title='Job Board API')),
]