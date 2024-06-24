from rest_framework import serializers
from .models import formData

#CREATE FORMDATA SERIALIZER FOR API INTEGRATION

class formDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = [
        "name","email","no_of_family","raised_amount","fund_breakdown","fund_url","comments","family_in_egypt"
        ]
class getDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = [
        "name","no_of_family","raised_amount","fund_breakdown","fund_url"
    ]