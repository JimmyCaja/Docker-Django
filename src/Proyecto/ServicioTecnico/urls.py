from django.urls import path, include
from .views import *
from ServicioTecnico.api.router import *

urlpatterns = [   
    #Correo
    path('send/', Send.as_view(), name='send'),
    #path('pdf/<id>/', pdf),
    
    # API
    path('api/equipo/', EquipoView.as_view(), name='equipo_list'),
    path('api/equipo/<int:id>', EquipoView.as_view(), name='equipo_process'),
    path('api/recibo/', ReciboView.as_view(), name='recibo_list'),
    path('api/recibo/<int:id>', ReciboView.as_view(), name='recibo_process'),

    path('api/', include(router.urls)),
    
    # PRINCIPAL
    path('', home, name="home"),
    path('Servicios/', servicios_view),
    path('ServicioMantenimiento', serviciomantenimiento_view),
    path('ServicioProgramas/', servicioprogramas_view),
    path('ServicioAntivirus/', servicioantivirus_view),
    path('ServicioSO/', servicioso_view),
    path('ServicioFormateo/', servicioformateo_view),

    path('productos/', productos_view),
    path('contactenos/', contactenos_view),
    path('registracion/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('error-facebook/', error_facebook, name="error_facebook"),
    path('social-auth/', include('social_django.urls', namespace='social')),
    
    # CLIENTES 

    path('Cliente/', listarClientes, name="listarClientes"),
    path('Cliente/registrar/', registrarCliente, name="registrarCliente"),
    path('Cliente/modificar/<id>/', modificarCliente, name="modificarCliente"),
    path('Cliente/eliminar/<id>/', eliminarCliente, name="eliminarCliente"),

    # EQUIPOS 

    path('Equipo/<aux>/', listarEquiposCliente, name="listarEquiposCliente"),
    path('Equipo/<aux>/registrar/', registrarEquipo, name="registrarEquipo"),
    path('Equipo/<aux>/modificar/<id>/', modificarEquipo, name="modificarEquipo"),
    path('Equipo/<aux>/eliminar/<id>/', eliminarEquipo, name="eliminarEquipo"),

    # RECIBOS 

    path('Recibo/', listarRecibos, name="listarRecibos"),
    path('Recibo/registrar/', registrarRecibo, name="registrarRecibo"),
    path('Recibo/modificar/<id>/', modificarRecibo, name="modificarRecibo"),
    path('Recibo/eliminar/<id>/', eliminarRecibo, name="eliminarRecibo"),

    # DIAGNOSTICO

    path('Diagnostico/', listarDiagnosticos, name="listarDiagnosticos"),
    path('Diagnostico/registrar/', registrarDiagnostico, name="registrarDiagnostico"),
    path('Diagnostico/modificar/<id>/', modificarDiagnostico, name="modificarDiagnostico"),
    path('Diagnostico/eliminar/<id>/', eliminarDiagnostico, name="eliminarDiagnostico"),

    # EMPLEADOS

    path('Empleado/', listarEmpleados, name="listarEmpleados"),
    path('Empleado/registrar/', registrarEmpleado, name="registrarEmpleado"),
    path('Empleado/modificar/<id>/', modificarEmpleado, name="modificarEmpleado"),
    path('Empleado/eliminar/<id>/', eliminarEmpleado, name="eliminarEmpleado"),

    # PEDIDOS

    path('Pedido/', listarPedidos, name="listarPedidos"),
    path('Pedido/registrar/', registrarPedido, name="registrarPedido"),
    path('Pedido/modificar/<id>/', modificarPedido, name="modificarPedido"),
    path('Pedido/eliminar/<id>/', eliminarPedido, name="eliminarPedido"),

    # PRODUCTOS

    path('Producto/', listarProductos, name="listarProductos"),
    path('Producto/registrar/', registrarProducto, name="registrarProducto"),
    path('Producto/modificar/<id>/', modificarProducto, name="modificarProducto"),
    path('Producto/eliminar/<id>/', eliminarProducto, name="eliminarProducto"),
    
    # SERVICIO

    path('Servicio/', listarServicios, name="listarServicios"),
    path('Servicio/registrar/', registrarServicio, name="registrarServicio"),
    path('Servicio/modificar/<id>/', modificarServicio, name="modificarServicio"),
    path('Servicio/eliminar/<id>/', eliminarServicio, name="eliminarServicio"),

    # PROVEEDOR

    path('Proveedor/', listarProvedores, name="listarProvedores"),
    path('Proveedor/registrar/', registrarProveedor, name="registrarProveedor"),
    path('Proveedor/modificar/<ruc>/', modificarProveedor, name="modificarProveedor"),
    path('Proveedor/eliminar/<ruc>/', eliminarProveedor, name="eliminarProveedor"),
    

]