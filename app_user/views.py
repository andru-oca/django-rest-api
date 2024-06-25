from django.contrib.auth.models import User # Modelo de Users predefinido por django
from .serializer import UserSerializer # Un serializador standar
from rest_framework import viewsets # permite generar las views para el access
from django.contrib.auth.hashers import make_password # permite hacer el hash del pass

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def perform_create(self, serializer):
        return serializer.save(password=make_password(serializer.validated_data['password']))