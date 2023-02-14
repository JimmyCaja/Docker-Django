from django.db import router
from rest_framework.routers import DefaultRouter
from ServicioTecnico.api.views import *

router = DefaultRouter()

router.register(prefix='users', basename='users', viewset = UserApiViewSet)

#router.register(prefix='equipo', basename='equipo', viewset = EquipoView)

#router.register(prefix='recibo', basename='recibo', viewset = ReciboView)

#router.register(prefix='estudiante', basename='estudiante', viewset=ReciboApiViewSet)