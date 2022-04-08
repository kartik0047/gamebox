from django import forms

from .models import *
#from Games.models import ClassInfo

#class GamesForm(forms.ModelForm):
    #class Meta:
        #model = Games
    

class CouponApplyForm(forms.Form):
     code = forms.CharField()