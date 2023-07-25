from django.db import models
from django.utils import timezone
# Create your models here.

#Categoria
class Categoria(models.Model):

    nombre = models.CharField(max_length=200, null=False, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-nombre',)

    def __str__(self):
        return self.nombre
    
    

#Etiqueta
class Etiqueta(models.Model):

    nombre = models.CharField(max_length=200, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-nombre',)

    def __str__(self):
        return self.nombre

 #Articulo   
class Articulo(models.Model):
    
    titulo = models.CharField(max_length=250, null=False)
    subtitulo = models.CharField(max_length=600, null=True, blank=True)
    fecha_actualiz = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(null= False, default=False)
    contenido = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='img/', default='img/post_default.jpeg')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    etiqueta = models.ForeignKey(Etiqueta,on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('-fecha_creacion',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()