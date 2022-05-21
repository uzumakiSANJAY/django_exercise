from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Message

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id','messages','created_at','updated_at','created_by']

