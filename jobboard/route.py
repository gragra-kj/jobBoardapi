from .views import JobViewSet,ApplicationViewset,CompanyViewSet,register_user,login_user
from django.urls import path,include
from rest_framework.routers import DefaultRouter

#from rest_framework.documentation import include_docs_urls


router=DefaultRouter()

router.register('jobs',JobViewSet,basename='job')
router.register('application',ApplicationViewset,basename='application')
router.register('company',CompanyViewSet,basename='company')

urlpatterns=[
    path('',include(router.urls)),
    path('register',register_user,name='register'),
    path('login/',login_user,name='login')
    #path('docs/', include_docs_urls(title='Job Board API')),
]