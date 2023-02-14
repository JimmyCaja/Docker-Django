from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def _str_(self) :
        return str(self.username)

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length = 50, verbose_name = 'Nombres')
    apellidos = models.CharField(max_length = 50, verbose_name = 'Apellidos')
    cedula = models.CharField(max_length = 10, verbose_name = 'Cedula')
    telefono = models.CharField(max_length = 9, verbose_name = 'Telefono')
    telefonoMovil = models.CharField(max_length = 10, verbose_name = 'TelefonoMovil')
    email = models.EmailField()
    direccion = models.CharField(max_length = 100, verbose_name = 'Direccion')

    def nombre_completo(self):
        return "{} {}".format(self.nombres, self.apellidos)
    
    def __str__(self):
        return self.nombre_completo()
    
    def __getitem__(self, key):
        return self.__dict__[key]

class Equipo(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 100, verbose_name = 'Descripción')
    marca = models.CharField(max_length = 50, verbose_name = 'Marca')
    modelo = models.CharField(max_length = 50, verbose_name = 'Modelo')
    numSerie = models.CharField(max_length = 14, verbose_name = 'Numero de Serie')
    observaciones = models.CharField(max_length = 500, verbose_name = 'Observaciones')
    
    def nombre(self):
        return "{} {}".format(self.descripcion, self.marca)
    
    def __str__(self):
        return self.nombre()

class Servicio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, verbose_name = 'Nombre')
    descripcion = models.CharField(max_length = 500, verbose_name = 'Descripción')
    valor = models.FloatField(verbose_name = 'Valor')

    def nombre_servicio(self):
        return "{} {}".format(self.nombre, self.valor)
    
    def __str__(self):
        return self.nombre_servicio()

opciones_roles = [
    [0, "Vendedor"],
    [1, "Tecnico"],
    [2, "admin2"]
]

class Empleado(models.Model):
    id = models.AutoField(primary_key = True)
    rol = models.IntegerField(choices=opciones_roles, verbose_name = 'Rol')
    nombres = models.CharField(max_length = 50, verbose_name = 'Nombres')
    apellidos = models.CharField(max_length = 50, verbose_name = 'Apellidos')
    cedula = models.CharField(max_length = 10, verbose_name = 'Cedula')
    email = models.EmailField()
    telefono = models.CharField(max_length = 10, verbose_name = 'Telefono')
    direccion = models.CharField(max_length = 100, verbose_name = 'Direccion')

    def nombre_completo(self):
        return "{} {} {}".format(self.rol, self.nombres, self.apellidos)
    
    def __str__(self):
        return self.nombre_completo()

class Diagnostico(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 500, verbose_name = 'Descripción')
    defecto = models.CharField(max_length = 150, verbose_name = 'Defecto')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)

    def nombre_diagnostico(self):
        return "{} {} {}".format(self.equipo, self.defecto, self.descripcion)
    
    def __str__(self):
        return self.nombre_diagnostico()
    
    def __getitem__(self, key):
        return self.__dict__[key]

class Proveedor(models.Model):
    ruc = models.CharField(primary_key = True, max_length = 13)
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
    email = models.EmailField()
    direccion = models.CharField(max_length = 100, verbose_name = 'Direccion')

    def nombre_proveedor(self):
        return "{} {}".format(self.ruc, self.nombre)
    
    def __str__(self):
        return self.nombre_proveedor()

opciones_productos = [
    [0, "Garantia"],
    [1, "Sin Garantia"]
]

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nroSerie = models.CharField(max_length = 13, verbose_name = 'Nro Serie')
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
    unidades = models.IntegerField(verbose_name = 'Unidades')
    precioCompra = models.FloatField(verbose_name = 'Precio Compra')
    precioVenta = models.FloatField(verbose_name = 'Precio Venta')
    marca = models.CharField(max_length = 50, verbose_name = 'Marca')
    modelo = models.CharField(max_length = 50, verbose_name = 'Modelo')
    tipo = models.IntegerField(choices=opciones_productos, verbose_name = 'Tipo')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def nombre_producto(self):
        return "{} {} {} {}".format(self.nroSerie, self.nombre, self.marca, self.tipo)
    
    def __str__(self):
        return self.nombre_producto()

class Pedido(models.Model):
    id = models.AutoField(primary_key = True)
    tiempoEntrega = models.CharField(max_length = 50, verbose_name = 'Tiempo Entrega')
    descripcion = models.CharField(max_length = 500, verbose_name = 'Descripción')
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tiempoEntrega

opciones_estadoRecibo = [
    [0, "Creado"],
    [1, "Progreso"],
    [3, "Facturado"]
]

opciones_tipo = [
    [0, "Venta"],
    [1, "Orden de Servicio"],
]

class Recibo(models.Model):
    id = models.AutoField(primary_key = True)
    fechaEmision = models.DateField(verbose_name = 'Fecha de Emisión')
    subTotalProductos = models.FloatField(verbose_name = 'Sub Total de Productos')
    valorTotal = models.FloatField(verbose_name = 'Valor Total')
    fechaCierre = models.DateField(verbose_name = 'Fecha de Cierre')
    estado = models.IntegerField(choices=opciones_estadoRecibo, verbose_name = 'Estado')
    subTotalServicios = models.FloatField(verbose_name = 'Sub Total Servicios')
    tipo = models.IntegerField(choices=opciones_tipo, verbose_name = 'Tipo')
    servicio = models.ManyToManyField(Servicio)
    diagnostico = models.OneToOneField(Diagnostico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

    def nombre_recibo(self):
        return "{} {}".format(self.id, self.fechaEmision)
    
    def __str__(self):
        return self.nombre_recibo()
    
    def __getitem__(self, key):
        return self.__dict__[str, key]
