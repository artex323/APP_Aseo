from django.shortcuts import render, get_object_or_404, redirect

from .models import Reserva, Servicio, Empleado, Cliente, Factura,Empleado
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

def menu_vista(request):
    opciones = ['Personal', 'Sedes', 'Administrar', 'Configuracion']
    return render(request, 'menu.html', {'opciones': opciones})



def lista_facturas(request):
    
    facturas = Factura.objects.all()
    context = {'facturas': facturas}
    return render(request, 'facturas/lista_facturas.html', context)

def detalle_factura(request, id_factura):
   
    factura = get_object_or_404(Factura, id_factura=id_factura)
    context = {'factura': factura}
    return render(request, 'facturas/detalle_factura.html', context)


def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'clientes/lista_clientes.html', context)


def detalle_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    context = {'cliente': cliente}
    return render(request, 'clientes/detalle_cliente.html', context)

def crear_cliente(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        
       
        Cliente.objects.create(
            nombre_cliente=nombre_cliente,
            email=email,
            telefono=telefono,
            direccion=direccion
        )
        return redirect('lista_clientes')  

    return render(request, 'clientes/crear_cliente.html')
# Crear una nueva factura
def crear_factura(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        monto_total = request.POST.get('monto_total')  # Cambié 'valor_total' por 'monto_total'
        id_reserva = request.POST.get('id_reserva')  # Recuperar la reserva seleccionada

        # Crear la factura con la reserva asociada
        Factura.objects.create(
            fecha=fecha,
            monto_total=monto_total,  
            id_reserva_id=id_reserva  
        )
        return redirect('lista_facturas')  

    reservas = Reserva.objects.all()  
    context = {'reservas': reservas}
    return render(request, 'facturas/crear_factura.html', context)


def lista_reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'reservas/lista_reservas.html', context)
def crear_reserva(request):
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        id_empleado = request.POST.get('id_empleado')  

        # Crear la reserva con el empleado asociado
        Reserva.objects.create(
            fecha=fecha,
            id_empleado_id=id_empleado 
        )
        return redirect('lista_reservas')  

    empleados = Empleado.objects.all()  
    context = {'empleados': empleados}
    return render(request, 'reservas/crear_reserva.html', context)

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/empleado_detail.html'
    context_object_name = 'empleado'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ['nombre_empleado', 'telefono', 'email', 'cargo']
    success_url = reverse_lazy('empleado_list')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ['nombre_empleado', 'telefono', 'email', 'cargo']
    success_url = reverse_lazy('empleado_list')

# Eliminar un empleado
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')