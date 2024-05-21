"""
URL configuration for HappyTails28 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, animals, exit, register, AnimalListView, registrar_animal, eliminar_animal, aliados, registrar_aliado, eliminar_aliado, editar_animal, edicion_animal, editar_aliado, edicion_aliado, consejitos, registrar_consejo, eliminar_consejo, editar_consejo, edicion_consejo, formularioA, formularioAnimal, formularioC, mostrarA

#app_name = 'happyTails28'

urlpatterns = [
    path('', home, name='home'),
    path('animals/', animals, name='animals'),
    path('aliados/', aliados, name='aliados'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('registrarAnimal/', registrar_animal),
    path('registrarAliado/', registrar_aliado),
    path('animals/mostrarA/eliminarAnimal/<int:idAnimal>', eliminar_animal),
    path('aliados/eliminarAliado/<int:idAliado>', eliminar_aliado),
    path('animals/mostrarA/editarAnimal/<int:idAnimal>', editar_animal),
    path('edicionAnimal/', edicion_animal),
    path('aliados/editarAliado/<int:idAliado>', editar_aliado),
    path('edicionAliado/', edicion_aliado),
    path('', AnimalListView.as_view(), name='gestion_animalitos'),
    path ('consejitos/', consejitos, name='consejitos'),
    path('registrarConsejo/', registrar_consejo),
    path('consejitos/eliminarConsejo/<int:idConsejo>', eliminar_consejo),
    path('consejitos/editarConsejo/<int:idConsejo>', editar_consejo),
    path('edicionConsejo/', edicion_consejo),
    path('aliados/registrarAliados/', formularioA),
    path('animals/registrarAnimales/', formularioAnimal),
    path('consejitos/registrarConsejos/', formularioC),
    path('animals/mostrarA/<int:idAnimal>', mostrarA),
    
]