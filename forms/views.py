from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import formData
from .serializers import formDataSerializer
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

#CREATE FORM USING POST REQUEST
@swagger_auto_schema(
        methods=["POST"],
        request_body=formDataSerializer,
        operation_description= "Create Forms"      
)
@api_view(["POST"])
def createForm(request):
    if request.method == "POST":
        create_form_serializer = formDataSerializer(data=request.data)
        if create_form_serializer.is_valid():
            create_form_serializer.save()
            return Response(create_form_serializer.data, status=status.HTTP_201_CREATED)
    return Response(create_form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET ALL FORMDATA using GET REQUEST
@api_view(["GET"])
def getAllForm(request):
    get_all_forms = formData.objects.all()
    if request.method == "GET":
        get_allform_serilizer = formDataSerializer(get_all_forms, many=True)
        return Response(get_allform_serilizer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#GET ONLY APPROVED FORMS TO DISPLAY
@api_view(["GET"])
def getApproved(request):
    get_approved = formData.objects.all().filter(approved=True)
    if request.method == "GET":
        get_allform_serilizer = formDataSerializer(get_approved, many=True)
        return Response(get_allform_serilizer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Unique forms using GET, PUT AND DELETE REQUEST
@swagger_auto_schema(
        methods=["PUT","DELETE"],
        request_body=formDataSerializer,
        operation_description= "Update and Delete Forms"      
)
@api_view(["GET","PUT","DELETE"])
def specificForm(request, pk):
    get_specific_form = get_object_or_404(formData, id=pk)
    if request.method =="GET":
        get_specific_serializer = formDataSerializer(get_specific_form)
        return Response(get_specific_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        update_form_serializer = formDataSerializer(get_specific_form, data=request.data)
        if update_form_serializer.is_valid():
            update_form_serializer.save()
            return Response(update_form_serializer.data, status=status.HTTP_202_ACCEPTED)
    
    elif request.method == "DELETE":
        get_specific_form.delete()
        return Response("Deleted")
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)