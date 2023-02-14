from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

from rest_framework.viewsets import ModelViewSet
from ServicioTecnico.models import *
from ServicioTecnico.api.serializers import *
from django.contrib.auth.models import User
#USUARIOS
class UserApiViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


#class ProfesorApiViewSet(ModelViewSet):
 #   serializer_class = ProfesorSerializer
  #  queryset = Profesor.objects.all()
class EquipoView(View):
    # Método que se ejecuta cada vez que se realiza una petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            equipos = list(Equipo.objects.filter(id=id).values())
            if len(equipos) > 0:
                equipo = equipos[0]
                datos = {'message': "Success", 'equipo': equipo}
            else:
                datos = {'message': "Profesores not found..."}
            
            return JsonResponse(datos)

        else:
            equipos = list(Equipo.objects.values())
            if len(equipos) > 0:
                datos = {'message': "Success", 'equipos': equipos}
            else:
                datos = {'message': "Profesores not found..."}
            
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Equipo.objects.create(descripcion=jd['descripcion'], marca=jd['marca'], modelo=jd['modelo'], numSerie=jd['numSerie'], observaciones=jd['observaciones'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

class ReciboView(View):
    # Método que se ejecuta cada vez que se realiza una petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            recibos = list(Recibo.objects.filter(id=id).values())
            if len(recibos) > 0:
                recibo = recibos[0]
                datos = {'message': "Success", 'recibo': recibo}
            else:
                datos = {'message': "Profesores not found..."}
            
            return JsonResponse(datos)

        else:
            recibos = list(Recibo.objects.values())
            if len(recibos) > 0:
                datos = {'message': "Success", 'recibos': recibos}
            else:
                datos = {'message': "Profesores not found..."}
            
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Recibo.objects.create(fechaEmision=jd['fechaEmision'], subTotalProductos=jd['subTotalProductos'], valorTotal=jd['valorTotal'], fechaCierre=jd['fechaCierre'], estado=jd['estado'], subTotalServicios=jd['subTotalServicios'], tipo=jd['tipo'], servicio=jd['servicio'], diagnostico=jd['diagnostico'], cliente=jd['cliente'], productos=jd['productos'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
