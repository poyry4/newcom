from django.shortcuts import render
from .models import categorys, commercial, imageCommercial
from .form import categorysForm, commercialForm, imageCommercialForm

# Create your views here.
def adminCommercial_view(request):
    form = commercialForm()
    return render(request, 'commercial/adminCommercial.htm', { 'form': form })

