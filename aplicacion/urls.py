from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Funcion de inicio
    path('inicio', index, name="inicio"),

    # Funciones de los models
    path('animales/', animal, name="animales"),
    path('dueños/', duenio, name="dueños"),
    path('veterinarios', veterinario, name="veterinarios"),
    path('sucursales/', sucursales, name="sucursales"),
    path('turnos/', turnos, name="turnos"),
    path('preguntasFrecuentes/', preguntasFrecuentes, name="preguntasFrecuentes"),

    #
        # Funciones de los forms
        path('animalForm/', animalForm, name="animalForm"),
        path('animalForm1/', animalForm, name="animalForm1"),
        #path('paciente_Form1/', pacienteForm1, name="pacienteform1"),
    #    path('hospital_Form1/', hospitalForm1, name="hospitalform1"),
    #     path('historial_Form1/', historialForm1, name="historialform1"),
    # #
        # Funciones de los forms de busqueda
        path('buscarAnimal/', buscarAnimal, name="buscarAnimal"),
        path('busqueda1/', busqueda1, name="busqueda1"),

    #
        # Urls de los Updates
        path('updateDueño/<id_duenio>/', updateDuenio, name="updateDueño"),
        path('deleteDueño/<id_duenio>/', deleteDuenio, name="deleteDueño"),
        path('createDueño/', createDuenio, name="createDueño"),


    # #
    #     # Urls Class Based Views
    #     path('paciente_list/', PacienteList.as_view(), name="pacientes"),
    #     path('create_paciente/', PacienteCreate.as_view(), name="create_paciente"),
    #     path('detail_paciente/<int:pk>/', PacienteDetail.as_view(), name="detail_paciente"),
    #     path('update_paciente/<int:pk>/', PacienteUpdate.as_view(), name="update_paciente"),
    #     path('delete_paciente/<int:pk>/', PacienteDelete.as_view(), name="delete_paciente"),
    #     path('delete_paciente/<int:pk>/', PacienteDelete.as_view(), name="delete_paciente"),

    # #
    #     # Urls Login/Logout
    #     path('login/', login_request, name="login"),
    #     path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    #     path('register/', register, name="register"),

    # #
    #     # Urls de edicion   
    #     path('editar_usuario/', perfilEdit, name="editar_usuario"),

    # #
    #     # Urls del Avatar
    #     path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]