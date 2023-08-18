from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Class-Based-View Imports
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Authentication Imports
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

# Funcion inicio
def index(request):
    return render(request, "aplicacion/base.html")

# Funcion Animal

def animal(request):
    ctx = {"animales": Animal.objects.all() }
    return render(request, "aplicacion/animales.html", ctx)

# Funcion Dueño

def duenio(request):
    ctx = {"dueños": Duenio.objects.all() }
    return render(request, "aplicacion/dueño.html", ctx)

# Funcion historial clinico

def veterinario(request):
    ctx = {"veterinario": Veterinario.objects.all() }
    return render(request, "aplicacion/veterinario.html", ctx)

# Funcion hospital

def sucursales(request):
    ctx = {"sucursal": Sucursales.objects.all() }
    return render(request, "aplicacion/sucursal.html", ctx)


def turnos(request):
    ctx = {"turnos": Turno.objects.all() }
    return render(request, "aplicacion/turnos.html", ctx)

# Funcion hospital

def preguntasFrecuentes(request):
    ctx = {"preguntasFrecuentes": PreguntasFrecuentes.objects.all() }
    return render(request, "aplicacion/preguntasFrecuentes.html", ctx)

#____________________________



# Funcion main formulario de Animal


def animalForm(request):
    if request.method == "POST":
        miForm = AnimalForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            animal = Animal(animal=informacion['animal'], raza=informacion['raza'],
                         nombre=informacion['nombre'], numeroContacto=request.POST['numeroContacto'])
            animal.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = AnimalForm()

    return render(request, "aplicacion/animalForm1.html", {"form":miForm}) 

def buscarAnimal(request):
    return render(request, "aplicacion/buscarAnimal.html")

# Funcion que muestra lo buscado en el formulario

def busqueda1(request):
    mascota = request.GET.get('Mascota', '')  # Obtiene el parámetro 'mascota' o una cadena vacía si no está presente
    if mascota:
        animales = Animal.objects.filter(animal__icontains=mascota)
        return render(request, "aplicacion/resultadoBusqueda.html", {"animales": animales, "mascota": mascota})
    return HttpResponse("No se ingresaron datos a buscar")

# Funcion formulario de paciente
# @login_required
# def pacienteForm1(request):
#     if request.method == "POST":
#         miForm = PacienteForm(request.POST)
#         print(miForm)
#         if miForm.is_valid():
#             informacion = miForm.cleaned_data
#             paciente= Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'],
#                             email=informacion['email']) 
#             paciente.save()
#             return render(request, "aplicacion/base.html")
#     else:
#         miForm = PacienteForm()
        
#     return render(request, "aplicacion/paciente_Form.html", {"form":miForm})S 

# Funcion formulario de hospital
# @login_required
# def duenioForm1(request):
#     if request.method == "POST":
#         miForm = DuenioForm(request.POST)
#         print(miForm)
#         if miForm.is_valid():
#             informacion = miForm.cleaned_data
#             duenio= Duenio(nombre=informacion['nombre'], direccion=informacion['direccion'])             
#             duenio.save()
#             return render(request, "aplicacion/base.html")
#     else:
#         miForm = HospitalForm()
        
#     return render(request, "aplicacion/hospitalForm1.html", {"form":miForm}) 

# Funcion formulario de hospital
# @login_required
# def hospitalForm1(request):
#     if request.method == "POST":
#         miForm = HospitalForm(request.POST)
#         print(miForm)
#         if miForm.is_valid():
#             informacion = miForm.cleaned_data
#             hospital= Hospital(nombre=informacion['nombre'], direccion=informacion['direccion'])             
#             hospital.save()
#             return render(request, "aplicacion/base.html")
#     else:
#         miForm = HospitalForm()
        
#     return render(request, "aplicacion/hospitalForm1.html", {"form":miForm}) 

# # Funcion formulario de Historial clinico
# @login_required
# def historialForm1(request):
#     if request.method == "POST":
#         miForm = HistorialForm(request.POST)
#         print(miForm)
#         if miForm.is_valid():
#             informacion = miForm.cleaned_data
#             historial= HistorialClinico(nombre=informacion['nombre'], apellido=informacion['apellido'],
#                                         fecha_nacimiento=informacion['fecha_nacimiento'],
#                                           contacto_emergencia=informacion['contacto_emergencia'])             
#             historial.save()
#             return render(request, "aplicacion/base.html")
#     else:
#         miForm = HistorialForm()
        
#     return render(request, "aplicacion/historialForm1.html", {"form":miForm}) 

# # Funcion formulario para buscar en la base de datos





# Funciones de Update

def updateDuenio(request, id_duenio):
    duenio = Duenio.objects.get(id=id_duenio)
    if request.method == "POST":
        miForm = DuenioForm(request.POST)
        if miForm.is_valid():
            duenio.nombre = miForm.cleaned_data.get('nombre')
            duenio.apellido = miForm.cleaned_data.get('apellido')
            duenio.email = miForm.cleaned_data.get('email')
            duenio.direccion = miForm.cleaned_data.get('direccion')
            duenio.telefono = miForm.cleaned_data.get('telefono')
            duenio.save()
            return redirect(reverse_lazy('dueños')) # Redirecciona a la url 'Dueños'
    else: 
        miForm = DuenioForm(initial={'nombre':duenio.nombre,
                                     'apellido': duenio.apellido,
                                     'email': duenio.email,
                                     'direccion': duenio.direccion,
                                     'telefono':duenio.telefono})
                                      
    return render(request, "aplicacion/dueñoForm.html", {'form': miForm}) 


def deleteDuenio(request, id_duenio):
    dueño = Duenio.objects.get(id=id_duenio)
    dueño.delete()
    return redirect(reverse_lazy('dueños'))


def createDuenio(request):
    if request.method == "POST":
        miForm = DuenioForm(request.POST)
        if miForm.is_valid():
            d_nombre = miForm.cleaned_data.get('nombre')
            d_apellido = miForm.cleaned_data.get('apellido')
            d_email = miForm.cleaned_data.get('email')
            d_direccion = miForm.cleaned_data.get('direccion')
            d_telefono = miForm.cleaned_data.get('telefono')
            
            dueño = Duenio( 
                            nombre=d_nombre,
                            apellido=d_apellido, 
                            email=d_email, 
                            direccion=d_direccion,
                            telefono=d_telefono,
                            
                            ) 
            dueño.save()
            return redirect(reverse_lazy('dueños'))
    else:
        miForm = DuenioForm()

    return render(request, "aplicacion/dueñoForm.html", {'form': miForm})

# # Class Based View

class AnimalList(ListView):
    model = Animal

class AnimalCreate(CreateView):
    model = Animal
    fields = ['animal', 'raza', 'nombre', 'numeroContacto', 'dueño']
    success_url = reverse_lazy('animales')


class AnimalDetail(DetailView):
    model = Animal

# class PacienteUpdate(LoginRequiredMixin, UpdateView):
#     model = Paciente
#     fields = ['nombre', 'apellido', 'email']
#     success_url = reverse_lazy('pacientes')
#     template_name = "aplicacion/update_paciente.html"

# class PacienteDelete(LoginRequiredMixin, DeleteView):
#     model = Paciente
#     success_url = reverse_lazy('pacientes')


# Logins, Logouts, Register

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, "mensaje": f"Ingresaste datos incorrectos"})
        else:  
            return render(request, "aplicacion/login.html", {'form': miForm, "mensaje": f"Ingresaste datos incorrectos"})           

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {'form': miForm})


def register(request):
    if request.method == 'POST':
        miForm = RegistroUsuariosForm(request.POST) 
        if miForm.is_valid():  
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        miForm = RegistroUsuariosForm() 

    return render(request, "aplicacion/registro.html", {"form": miForm})   


# Registracion usuarios
@login_required
def perfilEdit(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            usuario.email = miForm.cleaned_data('email')
            usuario.password1 = miForm.cleaned_data('password1')
            usuario.password2 = miForm.cleaned_data('password2')
            usuario.first_name = miForm.cleaned_data('first_name')
            usuario.last_name = miForm.cleaned_data('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {"mensaje": f"El usuario {usuario.username} se ha actualizado de manera correcta!"})
        else:
            return render(request, "aplicacion/editarForm.html", {"form": miForm})
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editUser.html", {"form": miForm, "usuario": usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarFormulario(request.POST, request.FILES)
        if miForm.is_valid():
            u = User.objects.get(username=request.user)
            #__ Eliminacion del Avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: # Si es mayor a 0 significa que ya hay un avatar
                avatarViejo[0].delete()

            #__ Creacion del nuevo Avatar
            avatar = Avatar(user=u, imagen=miForm.cleaned_data['imagen'])
            avatar.save()

            #__ Almacenamiento del nuevo avatar
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        miForm = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm})
from django.shortcuts import render

# Create your views here.
