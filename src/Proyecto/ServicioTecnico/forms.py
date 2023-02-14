from xml.dom import ValidationErr
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class CrearUsuarioForm(UserCreationForm):

    '''def clean_username(self):
        username = self.cleaned_data["username"]
        existe = User.objects.filter(username__iexact=username).exists()

        if existe:
            raise ValidationError("Este nombre de usuario ya existe")

        return username

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        existe = User.objects.filter(first_name__iexact=first_name).exists()

        if existe:
            raise ValidationError("Este/os Nombre/s ya registrado por otro Usuario")

        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        existe = User.objects.filter(last_name__iexact=last_name).exists()

        if existe:
            raise ValidationError("Este/os Apellido/s ya registrado por otro Usuario")

        return last_name

    def clean_email(self):
        email = self.cleaned_data["email"]
        existe = User.objects.filter(email__iexact=email).exists()

        if existe:
            raise ValidationError("El correo electrónico ingresado ya existe en otro Empleado")

        return email
'''
    class Meta: 
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }



class ClienteForm(forms.ModelForm):
    
    def clean_cedula(self):
        cedula = self.cleaned_data["cedula"]

        if len(cedula) != 10:
            raise ValidationError("Falta digitos en la cédula ingresada")

        return cedula
    
    def clean_telefonoMovil(self):
        telefonoMovil = self.cleaned_data["telefonoMovil"]

        if len(telefonoMovil) < 10:
            raise ValidationError("Falta digitos en el número de teléfono ingresado")

        return telefonoMovil


    class Meta:
        model = Cliente
        fields = '__all__'



class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'



class ReciboForm(forms.ModelForm):

    class Meta:
        model = Recibo
        fields = '__all__'

        widgets = {
            "fechaEmision": forms.SelectDateWidget(),
            "fechaCierre": forms.SelectDateWidget(),
        }



class DiagnosticoForm(forms.ModelForm):

    class Meta:
        model = Diagnostico
        fields = '__all__'



class EmpleadoForm(forms.ModelForm):

    '''def clean_apellidos(self):
        apellidos = self.cleaned_data["apellidos"]
        existe = Empleado.objects.filter(apellidos__iexact=apellidos).exists()

        if existe:
            raise ValidationError("Ya existe un empleado con los mismos apellidos")

        return apellidos'''

    def clean_cedula(self):
        cedula = self.cleaned_data["cedula"]
        #existe = Empleado.objects.filter(cedula__iexact=cedula).exists()

        if len(cedula) != 10:
            #if existe:
                #raise ValidationError("La cédula ingresada ya existe")
        #else:
            raise ValidationError("Falta digitos en la cédula ingresada")

        return cedula

    '''def clean_email(self):
        email = self.cleaned_data["email"]
        existe = Empleado.objects.filter(email__iexact=email).exists()

        if existe:
            raise ValidationError("El correo electrónico ingresado ya existe en otro Empleado")

        return email'''

    class Meta:
        model = Empleado
        fields = '__all__'



class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'



class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'



class ProductoForm(forms.ModelForm):

    '''def clean_nroSerie(self):
        nroSerie = self.cleaned_data["nroSerie"]
        existe = Producto.objects.filter(nroSerie__iexact=nroSerie).exists()

        if existe:
            raise ValidationError("Este número de Serie de producto ya fue registrado")

        return nroSerie

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre de producto ya existe")

        return nombre'''

    class Meta:
        model = Producto
        fields = '__all__'



class ServicioForm(forms.ModelForm):

    '''def clean_nombre(self):
        #nombre = self.cleaned_data["nombre"]
        #existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        #if existe:
        #    raise ValidationError("Este nombre de Servicio ya existe")

        #return nombre'''

    class Meta:
        model = Servicio
        fields = '__all__'

  