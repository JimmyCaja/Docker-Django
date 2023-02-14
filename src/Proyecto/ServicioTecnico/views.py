from pkgutil import get_data
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
#Correo
from django.views import View
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
#from xhtml2pdf import pisa
#OJO

#EMAIL
class Send(View):
    def get(self, request):
        return render(request, 'Mail/send.html')
    
    def post(self, request):
        email = request.POST.get('email')
        print(email)

        template = get_template('Mail/email-order-success.html')

        #Se renderiza el template y se envía parametros
        content = template.render({'email': email})

        #Se crea el correo(titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives (
            'Gracias por tu compra',
            'Hola, te enviamos un correo con tu recibo',
            settings.EMAIL_HOST_USER,
            [email]
        )

        msg.attach_alternative(content, 'text/html')
        msg.send()

        return render(request, 'Mail/send.html')

#pdf
# GENERAR PDF
'''
def pdf(request, id):
    recibo = Recibo.objects.get(id=id)
    template_path = 'pdf.html'
    data = {
        'rec': recibo,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Recibo.pdf"'
    # find the template and render it.
    template = get_template('Mail/email-order-success.html')
    html = template.render(data)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
'''
# REGISTRO

def registro(request):
    data = {
        'form': CrearUsuarioForm()
    }

    if request.method == 'POST':
        formulario = CrearUsuarioForm(data = request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            u = Usuario()
            u.user_id = usuario.id
            u.username = formulario.cleaned_data.get('username')
            u.password = formulario.cleaned_data.get('password1')
            u.save()

            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Te has registrado correctamete")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, "registration/registro.html", data)

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registracion/login.html',{})

def error_facebook(request):
    return render(request, 'registration/error_facebook')

# SERVICIOS
def servicios_view(request):
    return render(request, 'Servicio/servicios.html')

def serviciomantenimiento_view(request):
    return render(request, 'Servicio/mantenimiento.html')

def servicioprogramas_view(request):
    return render(request, 'Servicio/programas.html')

def servicioantivirus_view(request):
    return render(request, 'Servicio/antivirus.html')

def servicioso_view(request):
    return render(request, 'Servicio/so.html')

def servicioformateo_view(request):
    return render(request, 'Servicio/formateo.html')

def productos_view(request):
    return render(request, 'productos.html')

def contactenos_view(request):
    return render(request, 'contactenos.html')



""" CRUD CLIENTES """

@permission_required('ServicioTecnico.view_cliente')
def listarClientes(request):
    clientes = Cliente.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(clientes, 5)
        clientes = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': clientes,
        'paginator': paginator
    }
    return render(request, 'Cliente/index.html', data)

@permission_required('ServicioTecnico.add_cliente')
def registrarCliente(request):
    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Cliente Registrado Correctamente')
            return redirect(to = "listarClientes")
        else:
            data["form"] = formulario
    return render(request, 'Cliente/registrarCliente.html', data)

@permission_required('ServicioTecnico.change_cliente')
def modificarCliente(request, id):
    cliente = get_object_or_404(Cliente, id = id)
    data = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data = request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarClientes")
        data["form"] = formulario
    return render(request, 'Cliente/modificarCliente.html', data)

@permission_required('ServicioTecnico.delete_cliente')
def eliminarCliente(request, id):
    cliente = get_object_or_404(Cliente, id = id)
    cliente.delete()
    messages.success(request, "Cliente Eliminado Correctamente")
    return redirect(to = "listarClientes")



""" CRUD EQUIPOS """

@permission_required('ServicioTecnico.view_equipo')
def listarEquipos(request):
    equipos = Equipo.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(equipos, 5)
        equipos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': equipos,
        'paginator': paginator
    }
    return render(request, 'Equipo/index.html', data)

@permission_required('ServicioTecnico.add_equipo')
def registrarEquipo(request, aux):
    data = {
        'form': EquipoForm()
    }
    if request.method == 'POST':
        formulario = EquipoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro Guardado Correctamente")
            """return redirect(to = "listarEquiposCliente")"""
            return HttpResponseRedirect('/Equipo/'+str(aux)+'/')
        else:
            data["form"] = formulario
    return render(request, 'Equipo/registrarEquipo.html', data)

@permission_required('ServicioTecnico.change_equipo')
def modificarEquipo(request, id, aux):
    
    #if(aux=='1'):
        equipo = get_object_or_404(Equipo, id = id)
        data = {
            'form': EquipoForm(instance = equipo)
        }
        if request.method == 'POST':
            formulario = EquipoForm(data = request.POST, instance = equipo)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Cambios Guardados Correctamente")
                """return redirect(to = "listarEquiposCliente")"""
                return HttpResponseRedirect('/Equipo/'+str(aux)+'/')
            data["form"] = formulario
        return render(request, 'Equipo/modificarEquipo.html', data)
    #else:
    #    messages.error(request, "No tiene permiso para realizar esta acción")
    #    return HttpResponseRedirect('/Equipo/'+str(aux)+'/')

@permission_required('ServicioTecnico.delete_equipo')
def eliminarEquipo(request, id, aux):
    equipo = get_object_or_404(Equipo, id = id)
    equipo.delete()
    """return redirect(to = "listarEquiposCliente")"""
    return HttpResponseRedirect('/Equipo/'+str(aux)+'/')

""" EQUIPO CLIENTE """
def listarEquiposCliente(request, aux):
    
    user = get_object_or_404(User, id = aux)
    print("\nUsuario")
    print(user)
    print(aux)
    
    if ((aux == '1') or (str(user) == 'vendedor') or (str(user) == 'tecnico')):
        # listamos todos los equipos
        equipos = Equipo.objects.all()
        page = request.GET.get('page', 1)

        try:
            paginator = Paginator(equipos, 5)
            equipos = paginator.page(page)
        except:
            raise Http404

        data = {
            'entity': equipos,
            'paginator': paginator
        }
        return render(request, 'Equipo/index.html', data)

    else:

        # nombres == username
        cliente = get_object_or_404(Cliente, nombres = user) 

        # listamos recibos deacuerdo al cliente encontrado
        recibo = list(Recibo.objects.filter(cliente = cliente['id']).values())

        # listamos todos los diagnosticos que tienen recibos obtenido
        diagnosticos = []
        for re in recibo:
            print("recibos")
            print(re['diagnostico_id'])
            #diagnosticos.append(Diagnostico.objects.filter(id = int(re['diagnostico_id'])).values())
            diagnosticos.append(get_object_or_404(Diagnostico, id = int(re['diagnostico_id'])))

        for dia in diagnosticos:
            print("diagnostico")
            print(dia.defecto)
        
        # listamos todos los equipos de los diagnosticos obtenidos
        equipos = []
        for diagnostico in diagnosticos:
            print("equipo")
            print(diagnostico['equipo_id'])
            #diagnosticos.append(Diagnostico.objects.filter(id = int(re['diagnostico_id'])).values())
            equipos.append(get_object_or_404(Equipo, id = int(diagnostico['equipo_id'])))

        for equu in equipos:
            print("equipo")
            print(equu.descripcion)
        
        data = {'equipos': equipos, 'user': user,'cliente': cliente, 'recibo': recibo, 'diagnosticos': diagnosticos}
        return render(request, 'Equipo/index.html', data)


""" CRUD RECIBOS """

@permission_required('ServicioTecnico.view_recibo')
def listarRecibos(request):
    recibos = Recibo.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(recibos, 5)
        recibos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': recibos,
        'paginator': paginator
    }
    return render(request, 'Recibo/index.html', data)

@permission_required('ServicioTecnico.add_recibo')
def registrarRecibo(request):
    data = {
        'form': ReciboForm()
    }
    if request.method == 'POST':
        formulario = ReciboForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro Guardado Correctamente")
            return redirect(to = "listarRecibos")
        else:
            data["form"] = formulario
    return render(request, 'Recibo/registrarRecibo.html', data)

@permission_required('ServicioTecnico.change_recibo')
def modificarRecibo(request, id):
    recibo = get_object_or_404(Recibo, id = id)
    data = {
        'form': ReciboForm(instance = recibo)
    }
    if request.method == 'POST':
        formulario = ReciboForm(data = request.POST, instance = recibo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarRecibos")
        data["form"] = formulario
    return render(request, 'Recibo/modificarRecibo.html', data)

@permission_required('ServicioTecnico.delete_recibo')
def eliminarRecibo(request, id):
    recibo = get_object_or_404(Recibo, id = id)
    recibo.delete()
    return redirect(to = "listarEquipos")


""" CRUD DIAGNOSTICO """

@permission_required('ServicioTecnico.view_diagnostico')
def listarDiagnosticos(request):
    diagnosticos = Diagnostico.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(diagnosticos, 5)
        diagnosticos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': diagnosticos,
        'paginator': paginator
    }
    return render(request, 'Diagnostico/index.html', data)

@permission_required('ServicioTecnico.add_diagnostico')
def registrarDiagnostico(request):
    data = {
        'form': DiagnosticoForm()
    }
    if request.method == 'POST':
        formulario = DiagnosticoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Diagnostico Registrado Correctamente')
            return redirect(to = "listarDiagnosticos")
        else:
            data["form"] = formulario
    return render(request, 'Diagnostico/registrarDiagnostico.html', data)

@permission_required('ServicioTecnico.change_diagnostico')
def modificarDiagnostico(request, id):
    diagnosticos = get_object_or_404(Diagnostico, id = id)
    data = {
        'form': DiagnosticoForm(instance = diagnosticos)
    }
    if request.method == 'POST':
        formulario = DiagnosticoForm(data = request.POST, instance = diagnosticos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarDiagnosticos")
        data["form"] = formulario
    return render(request, 'Diagnostico/modificarDiagnostico.html', data)

@permission_required('ServicioTecnico.delete_diagnostico')
def eliminarDiagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id = id)
    diagnostico.delete()
    messages.success(request, "Diagnostico Eliminado Correctamente")
    return redirect(to = "listarDiagnosticos")


""" CRUD EMPLEADOS """

@permission_required('ServicioTecnico.view_empleado')
def listarEmpleados(request):
    empleados = Empleado.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(empleados, 5)
        empleados = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': empleados,
        'paginator': paginator
    }
    return render(request, 'Empleado/index.html', data)

@permission_required('ServicioTecnico.add_empleado')
def registrarEmpleado(request):
    data = {
        'form': EmpleadoForm()
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Empleado Registrado Correctamente')
            return redirect(to = "listarEmpleados")
        else:
            data["form"] = formulario
    return render(request, 'Empleado/registrarEmpleado.html', data)

@permission_required('ServicioTecnico.change_empleado')
def modificarEmpleado(request, id):
    empleado = get_object_or_404(Empleado, id = id)
    data = {
        'form': EmpleadoForm(instance = empleado)
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data = request.POST, instance = empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarEmpleados")
        data["form"] = formulario
    return render(request, 'Empleado/modificarEmpleado.html', data)

@permission_required('ServicioTecnico.delete_empleado')
def eliminarEmpleado(request, id):
    empleado = get_object_or_404(Empleado, id = id)
    empleado.delete()
    messages.success(request, "Empleado Eliminado Correctamente")
    return redirect(to = "listarEmpleados")


""" CRUD PEDIDOS """

@permission_required('ServicioTecnico.view_pedido')
def listarPedidos(request):
    pedidos = Pedido.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(pedidos, 5)
        pedidos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': pedidos,
        'paginator': paginator
    }
    return render(request, 'Pedido/index.html', data)

@permission_required('ServicioTecnico.add_pedido')
def registrarPedido(request):
    data = {
        'form': PedidoForm()
    }
    if request.method == 'POST':
        formulario = PedidoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Pedido Registrado Correctamente')
            return redirect(to = "listarPedidos")
        else:
            data["form"] = formulario
    return render(request, 'Pedido/registrarPedido.html', data)

@permission_required('ServicioTecnico.change_pedido')
def modificarPedido(request, id):
    pedido = get_object_or_404(Pedido, id = id)
    data = {
        'form': PedidoForm(instance = pedido)
    }
    if request.method == 'POST':
        formulario = PedidoForm(data = request.POST, instance = pedido)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarPedidos")
        data["form"] = formulario
    return render(request, 'Pedido/modificarPedido.html', data)

@permission_required('ServicioTecnico.delete_pedido')
def eliminarPedido(request, id):
    pedido = get_object_or_404(Pedido, id = id)
    pedido.delete()
    messages.success(request, "Pedido Eliminado Correctamente")
    return redirect(to = "listarPedidos")


""" CRUD PRODUCTOS """

@permission_required('ServicioTecnico.view_producto')
def listarProductos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'Producto/index.html', data)

@permission_required('ServicioTecnico.add_producto')
def registrarProducto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Producto Registrado Correctamente')
            return redirect(to = "listarProductos")
        else:
            data["form"] = formulario
    return render(request, 'Producto/registrarProducto.html', data)

@permission_required('ServicioTecnico.change_producto')
def modificarProducto(request, id):
    producto = get_object_or_404(Producto, id = id)
    data = {
        'form': ProductoForm(instance = producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarProductos")
        data["form"] = formulario
    return render(request, 'Producto/modificarProducto.html', data)

@permission_required('ServicioTecnico.delete_producto')
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")
    return redirect(to = "listarProductos")


""" CRUD SERVICIOS """

@permission_required('ServicioTecnico.view_servicio')
def listarServicios(request):
    servicios = Servicio.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(servicios, 5)
        servicios = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': servicios,
        'paginator': paginator
    }
    return render(request, 'Servicio/index.html', data)

@permission_required('ServicioTecnico.add_servicio')
def registrarServicio(request):
    data = {
        'form': ServicioForm()
    }
    if request.method == 'POST':
        formulario = ServicioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Servicio Registrado Correctamente')
            return redirect(to = "listarServicios")
        else:
            data["form"] = formulario
    return render(request, 'Servicio/registrarServicio.html', data)

@permission_required('ServicioTecnico.change_servicio')
def modificarServicio(request, id):
    servicio = get_object_or_404(Servicio, id = id)
    data = {
        'form': ServicioForm(instance = servicio)
    }
    if request.method == 'POST':
        formulario = ServicioForm(data = request.POST, instance = servicio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarServicios")
        data["form"] = formulario
    return render(request, 'Servicio/modificarServicio.html', data)

@permission_required('ServicioTecnico.delete_servicio')
def eliminarServicio(request, id):
    servicio = get_object_or_404(Servicio, id = id)
    servicio.delete()
    messages.success(request, "Servicio Eliminado Correctamente")
    return redirect(to = "listarServicios")



""" CRUD PROVEEDOR """

@permission_required('ServicioTecnico.view_proveedor')
def listarProvedores(request):
    provedores = Proveedor.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(provedores, 5)
        provedores = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': provedores,
        'paginator': paginator
    }
    return render(request, 'Proveedor/index.html', data)

@permission_required('ServicioTecnico.add_proveedor')
def registrarProveedor(request):
    data = {
        'form': ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.INFO, 'Proveedor Registrado Correctamente')
            return redirect(to = "listarProvedores")
        else:
            data["form"] = formulario
    return render(request, 'Proveedor/registrarProveedor.html', data)

@permission_required('ServicioTecnico.change_proveedor')
def modificarProveedor(request, ruc):
    proveedor = get_object_or_404(Proveedor, ruc = ruc)
    data = {
        'form': ProveedorForm(instance = proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data = request.POST, instance = proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cambios Guardados Correctamente")
            return redirect(to = "listarProvedores")
        data["form"] = formulario
    return render(request, 'Proveedor/modificarProveedor.html', data)

@permission_required('ServicioTecnico.delete_proveedor')
def eliminarProveedor(request, ruc):
    proveedor = get_object_or_404(Proveedor, ruc = ruc)
    proveedor.delete()
    messages.success(request, "Proveedor Eliminado Correctamente")
    return redirect(to = "listarProvedores")
