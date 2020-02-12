from django.contrib import admin

# Register your models here.
from .models import CatNews
from .models import News

admin.site.register(CatNews)

admin.site.register(News)