from django.contrib import admin
from .models import formData
# Register your models here.

@admin.register(formData)
class formDataAdmin(admin.ModelAdmin):
    list_display = [
        "name","email","no_of_family","raised_amount","fund_breakdown","fund_url","comments","family_in_egypt"
    ]
