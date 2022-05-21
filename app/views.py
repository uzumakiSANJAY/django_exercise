from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, MessageSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.throttling import UserRateThrottle

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle]
    queryset = models.Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):
        serializer = MessageSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        print(serializer.validated_data)
        # user = serializer.validated_data["created_by"]
        return Response(serializer.data)

    
   



