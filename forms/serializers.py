from rest_framework import serializers
from .models import formData

#CREATE FORMDATA SERIALIZER FOR API INTEGRATION

class formDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = [
        "id","name","email","no_of_family","raised_amount","fund_breakdown","fund_url","comments","family_in_egypt"
        ]

class getallDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = '__all__'
              
class approvedFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = ['id','approval']

class getallapprovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = formData
        fields = [
        "id","name","no_of_family","raised_amount","fund_url","approval"
        ]
