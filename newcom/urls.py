
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminsite/', include('adminsite.urls')) ,
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('commercial/', include('commercial.urls')),
    path('news/', include('news.urls')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)