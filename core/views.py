from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from user.models import Animal, Aliado, Consejos


# Create your views here.
def home (request):
    return render(request, 'core/home.html')

def formularioA (request):
    return render(request, 'formularios/registrarAliados.html')

def formularioAnimal (request):
    return render(request, 'formularios/registrarAnimal.html')

def formularioC (request):
    return render(request, 'formularios/registrarConsejo.html')

@login_required
def animals(request):
    listaAnimalitos = Animal.objects.all().order_by('fechaRescate')
    data = {
        'titulo': 'Listado de animales Facatativa',
        'animales': listaAnimalitos
    }
    return render(request, "core/animals.html", data)

@login_required
def aliados(request):
    listaAliados = Aliado.objects.all()
    data = {
        'titulo': 'Listado de aliados Facatativa',
        'aliados': listaAliados
    }
    return render(request, "core/aliados.html", data)

@login_required
def mostrarA(request, idAnimal):
    animal = Animal.objects.get(idAnimal=idAnimal)
    data = {
        'titulo': 'Mostrar animal',
        'animal': animal
    }
    return render(request, "core/mostrarA.html", data)

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

class AnimalListView(ListView):
    model = Animal
    template_name = 'core/animals.html'

    def get_queryset(self):
        return Animal.objects.all().order_by('fechaRescate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de animales Facatativa'
        return context
    
def registrar_animal(request):
    nombre = request.POST.get('txtNombre')
    raza = request.POST.get('txtRaza')
    estadoActual = bool(request.POST.get('estadoActualHidden'))
    estadoSalud = request.POST.get('txtEstadoSalud')
    ubicacion = request.POST.get('txtUbicacion')
    fechaRescate = request.POST.get('FechaRescate') 
    fechaAdopcion = request.POST.get('FechaAdopcion')
    numeroContacto = request.POST.get('txtNumeroContacto')

    # Obtener la imagen del formulario
    imagenAnimal = request.FILES.get('imagenAnimal')

    animal = Animal(nombre=nombre, raza=raza, estadoActual=estadoActual, estadoSalud=estadoSalud, ubicacion=ubicacion, fechaRescate=fechaRescate, fechaAdopcion=fechaAdopcion, numeroContacto=numeroContacto, imagenAnimal=imagenAnimal)
    animal.save()
    return redirect('animals')
    
def eliminar_animal(request, idAnimal):
    animal = Animal.objects.get(idAnimal=idAnimal)
    animal.delete()
    return redirect('animals')

def registrar_aliado(request):
    nombreEmpresa = request.POST.get('txtNombre')
    correoEmpresa = request.POST.get('txtCorreo')
    categoria = request.POST.get('categoria')
    ofrece = request.POST.get('ofrece')
    contraseña = request.POST.get('Contraseña')
    telefono = request.POST.get('Telefono')

    # Obtener la imagen del formulario
    imagenAliado = request.FILES.get('imagenAliado')

    aliado = Aliado(nombre_empresa=nombreEmpresa, correo=correoEmpresa, contraseña= contraseña, telefono=telefono, categoria=categoria, ofrece=ofrece, imagenAliado=imagenAliado)
    aliado.save()
    return redirect('aliados')


def eliminar_aliado(request, idAliado):
    aliado = Aliado.objects.get(idAliado=idAliado)
    aliado.delete()
    return redirect('aliados')

def editar_animal(request, idAnimal):
    animal = Animal.objects.get(idAnimal=idAnimal)
    data = {
        'titulo': 'Editar animales',
        'animal': animal
    }
    return render(request, "core/editarAnimal.html", data)

def edicion_animal(request):
    idAnimal = request.POST.get('idAnimal')
    nombre = request.POST.get('txtNombre')
    raza = request.POST.get('txtRaza')
    estadoActual = bool(request.POST.get('estadoActualHidden'))
    estadoSalud = request.POST.get('txtEstadoSalud')
    ubicacion = request.POST.get('txtUbicacion')
    fechaRescate = request.POST.get('FechaRescate') 
    fechaAdopcion = request.POST.get('FechaAdopcion')
    numeroContacto = request.POST.get('txtNumeroContacto')

    # Obtener la imagen del formulario
    imagenAnimal = request.FILES.get('imagenAnimal')

    animal = Animal.objects.get(idAnimal=idAnimal)
    animal.nombre = nombre
    animal.raza = raza
    animal.estadoActual = estadoActual
    animal.estadoSalud = estadoSalud
    animal.ubicacion = ubicacion
    animal.fechaRescate = fechaRescate
    animal.fechaAdopcion = fechaAdopcion
    animal.numeroContacto = numeroContacto
    animal.imagenAnimal = imagenAnimal
    animal.save()

    return redirect('animals')

def editar_aliado(request, idAliado):
    aliado = Aliado.objects.get(idAliado=idAliado)
    data = {
        'titulo': 'Editar aliados',
        'aliado': aliado
    }
    return render(request, "core/editarAliado.html", data)

def edicion_aliado(request):
    idAliado= request.POST.get('idAliado')
    nombreEmpresa = request.POST.get('txtNombre')
    correoEmpresa = request.POST.get('txtCorreo')
    categoria = request.POST.get('categoria')
    ofrece = request.POST.get('ofrece')
    contraseña = request.POST.get('Contraseña')
    telefono = request.POST.get('Telefono')

    # Obtener la imagen del formulario
    imagenAliado = request.FILES.get('imagenAliado')

    aliado = Aliado.objects.get(idAliado=idAliado)

    aliado.nombre_empresa = nombreEmpresa
    aliado.correo = correoEmpresa
    aliado.categoria = categoria
    aliado.ofrece = ofrece
    aliado.contraseña = contraseña
    aliado.telefono = telefono
    aliado.imagenAliado = imagenAliado
    aliado.save()

    return redirect('aliados')


@login_required
def consejitos(request):
    listaConsejos = Consejos.objects.all()
    data = {
        'titulo': 'Listado de consejos para tu mascota',
        'consejos': listaConsejos
    }
    return render(request, "core/consejitos.html", data)

def registrar_consejo(request):
    titulo = request.POST.get('txtTitulo')
    descripcion = request.POST.get('txtDescripcion')

    # Obtener la imagen del formulario
    imagenConsejo = request.FILES.get('imagenConsejo')

    consejo = Consejos(titulo=titulo, descripcion=descripcion, imagenConsejo=imagenConsejo)
    consejo.save()
    return redirect('consejitos')
    
def eliminar_consejo(request, idConsejo):
    consejo = Consejos.objects.get(idConsejo=idConsejo)
    consejo.delete()
    return redirect('consejitos')

def editar_consejo(request, idConsejo):
    consejo = Consejos.objects.get(idConsejo=idConsejo)
    data = {
        'titulo': 'Editar consejo',
        'consejos': consejo
    }
    return render(request, "core/editarConsejo.html", data)

def edicion_consejo(request):
    idConsejo = request.POST.get('idConsejo')
    titulo = request.POST.get('txtTitulo')
    descripcion = request.POST.get('txtDescripcion')

    # Obtener la imagen del formulario
    imagenConsejo = request.FILES.get('imagenConsejo')

    consejo = Consejos.objects.get(idConsejo=idConsejo)
    consejo.titulo = titulo
    consejo.descripcion = descripcion
    consejo.imagenConsejo = imagenConsejo
    consejo.save()

    return redirect('consejitos')