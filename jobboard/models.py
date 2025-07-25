from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JobModel(models.Model):
    JOB_TYPE=[
        ('fulltime','Full Time'),
        ('parttime','Part Time'),
        ('contract','Contract'),
        ('remote','Remote'),
    ]
    title=models.CharField(max_length=100)
    description=models.TextField()
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary_range=models.IntegerField()
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    posted_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    job_type=models.CharField(choices=JOB_TYPE)
    
    def __str__(self):
        return f'Apply for {self.title} position'
    
class ApplicationModel(models.Model):
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE)
    applicant=models.ForeignKey(User,on_delete=models.CASCADE)
    resume=models.FileField()
    coverletter=models.TextField()
    applied_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'You applied for the {self.job.title} job at {self.applied_at}'
    
    
class CompanyProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.SET_NULL)
    company_name=models.CharField(max_length=100)
    bio=models.TextField()
    website=models.URLField()
    location=models.CharField(max_length=100)  
    
    def __str__(self):
        return self.company_name      