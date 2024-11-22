from django.urls import path
from . import views

urlpatterns = [
    path('facturas/', views.lista_facturas, name='lista_facturas'),
    path('facturas/<int:id_factura>/', views.detalle_factura, name='detalle_factura'),
    path('facturas/crear/', views.crear_factura, name='crear_factura'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:id_cliente>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
]
