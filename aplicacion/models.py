from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
# Modelo Dueño

class Duenio(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=60)
    telefono = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}, vive en {self.direccion}. Contactar a traves de Telefono: {self.telefono} o Mail: {self.email}"  

# Modelo Animal, en este caso "mascota"

class Animal(models.Model):
    animal = models.CharField(max_length=25)
    raza = models.CharField(max_length=25)
    nombre = models.CharField(max_length=25)
    numeroContacto = models.IntegerField(null=False, blank=False)
    dueño = models.ForeignKey(Duenio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.animal} {self.raza}, llamado {self.nombre}, su dueño es {self.dueño}"       

# Modelo Veterinario    

class Veterinario(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"El veterinario {self.nombre} {self.apellido}, especializado en {self.especialidad}. Contacto: {self.email}"

# Modelo Sucursales   

class Sucursales(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField()
  
    def __str__(self):
        return f"Sucursal: {self.nombre}, {self.direccion}"  
    
# Modelo Turno   

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    mascota = models.ForeignKey(Animal, on_delete=models.CASCADE)
    situacion = models.CharField(max_length=25)

    def __str__(self):
        return f"El turno para {self.mascota} es el dia {self.fecha} a las {self.hora}, debido a {self.situacion}"
    
class PreguntasFrecuentes(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()
    
    def __str__(self):
        return f"Tu pregunta ha sido {self.pregunta}, esta es la mejor respuesta que podemos ofrecerte!, {self.respuesta}" 
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.imagen}]"
        from django.db import models

# Create your models here.
