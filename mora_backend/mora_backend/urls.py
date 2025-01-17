from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

def home_redirect(request):
    return HttpResponseRedirect('http://127.0.0.1:5500/index.html')

urlpatterns = [
    path('api/', include('api.urls')),
    path('users/', include('users.urls')),
    path('',home_redirect),
    path('admin/',admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)