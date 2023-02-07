from django.shortcuts import render
from django.http import HttpResponse
from AppAbrigate.models import *
from AppAbrigate.forms import *

# Create your views here.
def inicio(request):
    return render(request, 'AppAbrigate/inicio.html')

def productos(request):
   return render(request, 'AppAbrigate/productos.html')

def clientes(request):
    return render(request, 'AppAbrigate/clientes.html')

def carrito(request):
    return render(request, 'AppAbrigate/carrito.html')

def agregar_producto(request):
    if request.method == 'POST':
        frmAgregarProducto = Frm_agregar_producto(request.POST)
        if frmAgregarProducto.is_valid(): #validar la integridad de los datos en el formulario
            infoDic = frmAgregarProducto.cleaned_data #Los datos del formulario se agregan a un diccionario
            prodcuto1 = Productos(nombre = infoDic['nombre'], 
            descripcion = infoDic['descripcion'], 
            departamento = infoDic['departamento'],
            talla = infoDic['talla'],
            color = infoDic['color'],
            tipo = infoDic['tipo'],
            existencia = infoDic['existencia'])
            #imagen = infoDic['imagen'])
            prodcuto1.save()
            return render(request, 'AppAbrigate/inicio.html')
    else:
        frmAgregarProducto = Frm_agregar_producto()
    return render(request, 'AppAbrigate/formAgregarProducto.html', {'frmProducto':frmAgregarProducto})

def agregar_cliente(request):
    if request.method == 'POST':
        frmAgregarCliente = Frm_agregar_cliente(request.POST)
        if frmAgregarCliente.is_valid(): #validar la integridad de los datos en el formulario
            infoDic = frmAgregarCliente.cleaned_data #Los datos del formulario se agregan a un diccionario
            cliente1 = Clientes(nombre = infoDic['nombre'], 
            edad = infoDic['edad'], 
            correo = infoDic['correo'],
            calleYNumero = infoDic['calleYNumero'],
            colonia = infoDic['colonia'],
            municipio = infoDic['municipio'],
            estado = infoDic['estado'],
            pais = infoDic['pais'],
            cp = infoDic['cp'])
            cliente1.save()
            return render(request, 'AppAbrigate/inicio.html')
    else:
        frmAgregarCliente = Frm_agregar_cliente()
    return render(request, 'AppAbrigate/formAgregarCliente.html', {'frmCliente':frmAgregarCliente})

def agregar_carrito(request):
    if request.method == 'POST':
        frmAgregarCarrito = Frm_agregar_carrito(request.POST)
        if frmAgregarCarrito.is_valid(): #validar la integridad de los datos en el formulario
            infoDic = frmAgregarCarrito.cleaned_data #Los datos del formulario se agregan a un diccionario
            carrito1 = Carrito(producto = infoDic['producto'],
            precio = infoDic['precio'], 
            cantidad = infoDic['cantidad'], 
            iva = infoDic['iva'])
            carrito1.save()
            return render(request, 'AppAbrigate/inicio.html')
    else:
        frmAgregarCarrito = Frm_agregar_carrito()
    return render(request, 'AppAbrigate/formAgregarCarrito.html', {'frmCarrito':frmAgregarCarrito})

def buscar_producto(request):
    return render(request, 'AppAbrigate/buscarProducto.html')

def resultados_busqueda_productos(request):
    # return HttpResponse(f"El producto que buscas es: {request.GET['producto']}")
    if request.GET['nombre']:
        productoBuscado = request.GET['nombre']
        productos = Productos.objects.filter(nombre__icontains=productoBuscado)
        return render(request, 'AppAbrigate/resultadosBusquedaProductos.html', {'productos':productos, 'resultado':productoBuscado})
    else:
        mensaje = '¡No hay datos para buscar!'
    return HttpResponse(mensaje)
    # return render(request, 'AppAbrigate/resultadosBusquedaProductos.html')