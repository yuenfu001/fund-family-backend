from rest_framework import serializers
from .models import formData

#CREATE FORMDATA SERIALIZER FOR API INTEGRATION

class formDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = "__all__"

class getDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = "__all__"