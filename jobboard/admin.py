from django.contrib import admin

# Register your models here.
from .models import JobModel,ApplicationModel,CompanyProfile

admin.site.register(JobModel)
admin.site.register(ApplicationModel)
admin.site.register(CompanyProfile)