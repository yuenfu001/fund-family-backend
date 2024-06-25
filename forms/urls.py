from django.urls import path
from . import views

urlpatterns = [
    path("allform/", views.getAllForm, name="get_all_form"),
    path("create_form/", views.createForm, name="create_form"),
    path("get_only_approved/", views.getAllApprovedForm, name="get_only"),
    path("approve_form/", views.getApproval, name="approve_form"),
    # path("get_form/<str:pk>/", views.specificForm, name="specific_form"),
]
