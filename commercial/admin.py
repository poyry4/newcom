from django.contrib import admin

from .models import imageCommercial
from .models import commercial, categorys

admin.site.register(imageCommercial)

admin.site.register(commercial)

admin.site.register(categorys)