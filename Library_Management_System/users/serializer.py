from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'Email', ' Date_of_membership', 'Active_Status']
        read_only_fields = ['id', ' Date_of_membership']