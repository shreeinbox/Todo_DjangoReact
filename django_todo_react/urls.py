
# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]
