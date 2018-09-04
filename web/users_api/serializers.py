from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    min_len=8

    class Meta:
        model = User
        fields = ('id','email', 'username','phone', 'school_id','career','followers','following','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user_ = User(
            email=validated_data['email'],
            username=validated_data['username'],
            phone=validated_data['phone'],
            school_id=validated_data['school_id'],
        )

        user_.set_password(validated_data['password'])
        user_.save()

        return user_