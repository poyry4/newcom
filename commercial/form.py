from django import forms
from .models import categorys, commercial, imageCommercial

class commercialForm(forms.ModelForm):
    class Meta:
        model = commercial
        fields = '__all__'

class imageCommercialForm(forms.ModelForm):
    class Meta:
        model = imageCommercial
        fields = '__all__'

class categorysForm(forms.ModelForm):
    class Meta:
        model = categorys
        fields = '__all__'   
