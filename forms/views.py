from django.shortcuts import render,get_object_or_404,redirect
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import formData
from .serializers import formDataSerializer,getallDataSerializer,getallapprovedSerializer
from .forms import ApprovalFrom
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
        get_allform_serilizer = getallDataSerializer(get_all_forms, many=True)
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
    
# #GET ONLY APPROVED FORMS TO DISPLAY
# @swagger_auto_schema(
#         methods=["PUT"],
#         request_body=approvedFormDataSerializer,
#         operation_description= "Approved Forms"      
# )
# @api_view(["PUT"])
def getApproval(request,pk):
    get_specific_form = get_object_or_404(formData, id=pk)
    if request.method == "POST":
        get_approved_form = ApprovalFrom(request.POST, instance=get_specific_form)
        if get_approved_form.is_valid():
            get_approved_form.save()
            return redirect("allform")
    else:
        get_approved_form = ApprovalFrom(instance=get_specific_form)
    context = {
        "form":get_approved_form
    }
    return render(request, "approval.html", context)


#GET ALL Approved forms using GET REQUEST
@api_view(["GET"])
def getAllApprovedForm(request):
    get_all_approved_forms = formData.objects.all().filter(approval=True)
    if request.method == "GET":
        get_allform_serilizer = getallapprovedSerializer(get_all_approved_forms, many=True)
        return Response(get_allform_serilizer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)    

    
