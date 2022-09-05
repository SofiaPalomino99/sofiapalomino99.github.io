from xml.dom.minidom import Document
from django.urls import path #Esto se agrega 
from . import views
from django.conf import settings 
from django.contrib.staticfiles.urls import static

#Cuando el usuario acceda al servidor entrará a inicio y se va a mostrar
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name= 'nosotros'), 
    path('libros', views.libros, name ='libros'), 
    path('crear/libros', views.crear, name ='crear'), 
    path('eliminar/<int:id>', views.eliminar, name ='eliminar'), 
    path('libros/editar/<int:id>', views.editar, name ='editar'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Esto se coloca cuando queremos mostrar imagenes 
