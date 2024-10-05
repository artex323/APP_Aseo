from django.shortcuts import render

# Create your views here.

def menu_vista(request):
    opciones = ['Personal', 'Sedes', 'Administrar', 'Configuracion']
    return render(request, 'menu.html', {'opciones': opciones})

