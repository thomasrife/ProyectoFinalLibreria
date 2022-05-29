from curses.ascii import isblank
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from Libreria.forms import AutorForm, BuscarAutoresForm, LibroForm, EditorialForm

from Libreria.models import Autor, Editorial, Libro

def index(request):
    autores = Autor.objects.all()
    template = loader.get_template('Libreria/lista_autores.html')
    context = {
        'autor': autores,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            pais = form.cleaned_data['pais']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            Autor(nombre=nombre, apellido=apellido, pais=pais, fecha_nacimiento=fecha_nacimiento).save()

            return HttpResponseRedirect("/Libreria/")
    elif request.method == "GET":
        form = AutorForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'libreria/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        autor = Autor.objects.filter(id=int(identificador)).first()
        if autor:
            autor.delete()
        return HttpResponseRedirect("/Libreria/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass

def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarAutoresForm()
        return render(request, 'Libreria/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarAutoresForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            autor = Autor.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'Libreria/lista_autores.html', {"autor": autor})

def index_libro(request):
    libro = Libro.objects.all()
    template = loader.get_template('Libreria/lista_libros.html')
    context = {
        'libro': libro,
    }
    return HttpResponse(template.render(context, request))


def agregar_libro(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form_libro = LibroForm(request.POST)
        if form_libro.is_valid():

            titulo = form_libro.cleaned_data['titulo']
            autor = form_libro.cleaned_data['autor']
            editorial = form_libro.cleaned_data['editorial']
            fecha_de_publicacion = form_libro.cleaned_data['fecha_de_publicacion']
            isbn = form_libro.cleaned_data["isbn"]
            Libro(titulo=titulo, autor=autor, editorial=editorial, fecha_de_publicacion=fecha_de_publicacion, isbn=isbn).save()

            return HttpResponseRedirect("/Libreria/libros/")
    elif request.method == "GET":
        form_libro = LibroForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'libreria/form_carga_libro.html', {'form_libro': form_libro})


def borrar_libro(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        libro = Libro.objects.filter(id=int(identificador)).first()
        if libro:
            libro.delete()
        return HttpResponseRedirect("/Libreria/libros/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_libro(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass

def buscar_libro(request):
    if request.method == "GET":
        form_busqueda = BuscarAutoresForm()
        return render(request, 'Libreria/form_busqueda_libro.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarAutoresForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            libro = Libro.objects.filter(titulo__icontains=palabra_a_buscar)

        return  render(request, 'Libreria/lista_libros.html', {"libro": libro})

def index_editorial(request):
    editorial = Editorial.objects.all()
    template = loader.get_template('Libreria/lista_editorial.html')
    context = {
        'editorial': editorial,
    }
    return HttpResponse(template.render(context, request))


def agregar_editorial(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form_editorial = EditorialForm(request.POST)
        if form_editorial.is_valid():

            nombre_editorial = form_editorial.cleaned_data['nombre_editorial']
            pais_editorial = form_editorial.cleaned_data['pais_editorial']
            email = form_editorial.cleaned_data['email']
            Editorial(nombre_editorial=nombre_editorial, pais_editorial=pais_editorial, email=email).save()

            return HttpResponseRedirect("/Libreria/editorial/")
    elif request.method == "GET":
        form_editorial = EditorialForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'libreria/form_carga_editorial.html', {'form_editorial': form_editorial})


def borrar_editorial(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        editorial = Editorial.objects.filter(id=int(identificador)).first()
        if editorial:
            editorial.delete()
        return HttpResponseRedirect("/Libreria/editorial/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_editorial(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass

def buscar_editorial(request):
    if request.method == "GET":
        form_busqueda_editorial = BuscarAutoresForm()
        return render(request, 'Libreria/form_busqueda_editorial.html', {"form_busqueda_editorial": form_busqueda_editorial})

    elif request.method == "POST":
        form_busqueda_editorial = BuscarAutoresForm(request.POST)
        if form_busqueda_editorial.is_valid():
            palabra_a_buscar = form_busqueda_editorial.cleaned_data['palabra_a_buscar']
            editorial = Editorial.objects.filter(nombre_editorial__icontains=palabra_a_buscar)

        return  render(request, 'Libreria/lista_editorial.html', {"editorial": editorial})