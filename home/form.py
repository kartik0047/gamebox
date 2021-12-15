from django import forms

from .models import *
#from Games.models import ClassInfo

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
       # exclude = ['registration_no', 'status', 'personal_info', 'address_info', 'guardian_info', 'emergency_contact_info', 'previous_academic_info', 'previous_academic_certificate', 'is_delete']
        # widgets = {
        #     'class_info': forms.Select(attrs={'class': 'form-control'})
        # }