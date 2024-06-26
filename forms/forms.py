from django import forms
from .models import formData


class ApprovalFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set readonly attributes for all fields except 'approved'
        for field_name, field in self.fields.items():
            if field_name != 'approval':
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True
    
    class Meta:
        model = formData
        fields = "__all__"