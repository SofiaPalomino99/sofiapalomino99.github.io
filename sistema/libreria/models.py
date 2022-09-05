from django.db import models
#para capturar la estructua de la taba libros 
# Create your models here.
#todo esto se agrega, instrucciones, modelo donde se van a agregar. da la pauta de lo que se va a crear en el administrador
class Libro(models.Model): 
    id= models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen= models.ImageField(upload_to= 'imagenes/', verbose_name='Imagen', null=True, ) #Va a crear la carpeta imagenes
    descripcion = models.TextField(verbose_name='Descripcion', null=True) 
    
    def __srt__ (self): 
        fila= "Titulo: " + self.titulo + "-" + "Descripción: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
