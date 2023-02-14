"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ServicioTecnico import views, models
from rest_framework import routers, serializers, viewsets

from django.contrib.auth.models import User

#API Users propia de DJANGO - Problema:Encripta claves
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username', 'password']

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

#API Usuarios
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = views.Usuario
        fields = ['url','user_id', 'username', 'password']

# ViewSets define the view behavior.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = views.Usuario.objects.all()
    serializer_class = UsuarioSerializer

#API Equipo
class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Equipo
        fields = ['url','id', 'descripcion', 'marca', 'modelo']

# ViewSets define the view behavior.
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = models.Equipo.objects.all()
    serializer_class = EquipoSerializer

#API RECIBO
class ReciboSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Recibo
        fields = ['url','id', 'fechaEmision', 'valorTotal', 'tipo']

# ViewSets define the view behavior.
class ReciboViewSet(viewsets.ModelViewSet):
    queryset = models.Recibo.objects.all()
    serializer_class = ReciboSerializer


router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Equipo', EquipoViewSet)
router.register(r'Recibo', ReciboViewSet)

urlpatterns = [   
    #path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('', include('ServicioTecnico.urls')),
    #path('cliente/', cliente),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('apiu/', include(router.urls)),
]