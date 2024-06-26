from django.urls import path
from . import views

urlpatterns = [
    path("approve_form/<str:pk>/", views.getApproval, name="approve_form"),
    path("create_form/", views.createForm, name="create_form"),
    path("allform/", views.getAllForm, name="get_all_form"),
    path("get_only_approved/", views.getAllApprovedForm, name="get_only"),
    # path("get_form/<str:pk>/", views.specificForm, name="specific_form"),
]
