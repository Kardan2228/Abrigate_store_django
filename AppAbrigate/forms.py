from django import forms

class Frm_agregar_producto(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    departamento = forms.CharField()
    talla = forms.CharField()
    color = forms.CharField()
    tipo = forms.CharField()
    existencia = forms.IntegerField()
    #imagen = forms.ImageField()


class Frm_agregar_cliente(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    correo = forms.EmailField()
    calleYNumero = forms.CharField()
    colonia = forms.CharField()
    municipio = forms.CharField()
    estado = forms.CharField()
    pais = forms.CharField()
    cp = forms.IntegerField()

class Frm_agregar_carrito(forms.Form):
    producto = forms.IntegerField()
    precio = forms.DecimalField()
    cantidad = forms.IntegerField()
    iva = forms.DecimalField()

