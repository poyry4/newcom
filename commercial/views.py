from django.shortcuts import render
from .models import categorys, commercial, imageCommercial
from .form import categorysForm, commercialForm, imageCommercialForm

# Create your views here.
def adminCommercial_view(request):
    if request.method == 'POST':
         form = commercialForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('commercial:adminCommercial')
    else:    
        form = commercialForm()
        return render(request, 'commercial/adminCommercial.htm', { 'form': form })

