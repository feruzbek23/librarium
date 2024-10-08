from rest_framework import serializers
from account import models


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = (
            "id",
            "name",
            "email",  
            "books_count",
            "password",
        )
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)