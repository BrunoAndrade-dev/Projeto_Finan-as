from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha cria o prefixo: /api/analisador/
    path('api/analisador/', include('analisador.api.urls')),
]