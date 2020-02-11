from django.urls import path
from . import views

app_name = 'cimmercial'

urlpatterns = [
    path('admin/commercial/', views.adminCommercial_view, name="adminCommercial"),
  
]
