from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Modelserializer):
    class Meta:
        model  = User
        fields = ['id', 'unit']