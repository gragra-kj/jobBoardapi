from rest_framework import serializers
from .models import JobModel,ApplicationModel,CompanyProfile

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class JobSerializer(serializers.ModelSerializer):
    posted_by=UserSerializer(read_only=True)
    class Meta:
        model=JobModel
        fields=['id','title','description','company_name','location','job_type','salary','posted_by','posted_at','is_active','remote_option','job_expiry']
        
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['posted_by'] = request.user
        return super().create(validated_data)
    
    
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplicationModel
        fields=['id','job','applicant','resume','coverletter','applied_at']    
        read_only_fields = ['applicant', 'applied_at']
        
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['applicant'] = request.user
        return super().create(validated_data)    
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyProfile
        fields=['id','user','company_name','bio','website','location','company_logo']        