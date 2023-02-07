from django.urls import path
from AppAbrigate.views import *

urlpatterns = [
    path('inicio/', inicio, name = 'Inicio'),
    path('productos/', productos, name = 'Productos'),
    path('clientes/', clientes, name = 'Clientes'),
    path('carrito/', carrito, name = 'Carrito'),
    path('agregar_producto/', agregar_producto, name="AgregarProducto"),
    path('agregar_cliente/', agregar_cliente, name="AgregarCliente"),
    path('agregar_carrito/', agregar_carrito, name="AgregarCarrito"),
    path('buscar_producto/', buscar_producto, name='BuscarProducto'),
    path('resultados_productos/', resultados_busqueda_productos, name="ResultadosProductos"),
]
