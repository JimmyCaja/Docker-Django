from django.contrib import admin
from .models import *

class clienteAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos']
    list_display = ('id', 'nombres', 'apellidos', 'cedula')

class equipoAdmin(admin.ModelAdmin):
    search_fields = ['descripcion', 'marca']
    list_display = ('id', 'descripcion', 'marca', 'observaciones')

class reciboAdmin(admin.ModelAdmin):
    search_fields = ['id', 'fechaEmision']
    list_display = ('id', 'fechaEmision', 'fechaCierre', 'valorTotal', 'tipo')

class DiagnosticoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id', 'descripcion', 'defecto')

class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombres', 'apellidos', 'cedula']
    list_display = ('id', 'nombres', 'apellidos', 'cedula', 'email', 'telefono')
    
class PedidoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'tiempoEntrega']
    list_display = ('id', 'tiempoEntrega', 'descripcion')

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nroSerie', 'nombre', 'marca', 'modelo']
    list_display = ('id', 'nroSerie', 'nombre', 'unidades', 'precioCompra', 'precioVenta', 'marca', 'modelo', 'proveedor')

class ServicioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'valor']
    list_display = ('id', 'nombre', 'descripcion', 'valor')


admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Recibo)
admin.site.register(Diagnostico)

admin.site.register(Empleado)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Servicio)