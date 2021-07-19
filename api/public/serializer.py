from rest_framework import serializers

from .models import Public

class PublicSerializer(serializers.Modelserializer):
    class Meta:
        model  = Public
        fields = "__all__"