from django.shortcuts import render, redirect
from django.http import HttpResponse #Esto se agrega
from .models import Libro
from .forms import LibroForm

# Create your views here.
def inicio(request): #Funcion a donde se le envía una solicitud (request)
    return HttpResponse("<h1> Bienvenido a la libreria <\h1>")

def nosotros(request):
    return render(request, 'paginas/nosotros.html') #Busca un archivo nosotros.html, accede directamente a 
                                                    #templates, dentro de la carpeta paginas
def libros(request):
    libros=Libro.objects.all() #Esto se modifica despues de modificar models
    return render(request, 'libros/index.html', {'libros':libros}) 

def inicio(request): 
    return render(request, 'paginas/inicio.html')

def crear(request): 
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid(): 
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request,id): 
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method =='POST': 
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario':formulario})

def eliminar(request,id): 
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')