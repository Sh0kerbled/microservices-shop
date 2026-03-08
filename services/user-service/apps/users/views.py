from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, UserProfile
from .serializers import (
    UserWithProfileSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer
)