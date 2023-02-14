from rest_framework.serializers import ModelSerializer
from ServicioTecnico.models import *
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff' ]

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'descripcion', 'marca', 'modelo', 'numSerie', 'observaciones']

class ReciboSerializer(ModelSerializer):
    class Meta:
        model = Recibo
        fields = ['id', 'fechaEmision', 'subTotalProductos', 'valorTotal', 'fechaCierre', 'estado', 'subTotalServicios', 'tipo', 'servicio', 'diagnostico', 'cliente', 'productos']

