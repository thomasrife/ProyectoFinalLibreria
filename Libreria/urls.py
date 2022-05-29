from django.urls import path
from Libreria import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('buscar/', views.buscar, name="buscar"),
    path('libros/', views.index_libro, name="libros"),
    path('libros/agregar/', views.agregar_libro, name="agregar_libro"),
    path('libros/borrar/<identificador>', views.borrar_libro, name="borrar_libro"),
    path('libros/buscar/', views.buscar_libro, name="buscar_libro"),
    path('editorial/', views.index_editorial, name="editorial"),
    path('editorial/agregar/', views.agregar_editorial, name="agregar_editorial"),
    path('editorial/borrar/<identificador>', views.borrar_editorial, name="borrar_editorial"),
    path('editorial/buscar/', views.buscar_editorial, name="buscar_editorial"),
]
