from rest_framework import serializers
from .models import formData,approvedForm

#CREATE FORMDATA SERIALIZER FOR API INTEGRATION

class formDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = '__all__'
        
class approvedFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = approvedForm
        fields = [
        "form","approval"
        ]

class getallapprovedFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = approvedForm
        fields = [
        "form","approval"
        ]

class getDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = [
        "name","no_of_family","raised_amount","fund_breakdown","fund_url"
    ]