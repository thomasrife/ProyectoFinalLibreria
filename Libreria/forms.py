from django import forms
from pandas import notnull

class AutorForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    pais = forms.CharField(label="Pais", max_length=100)
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))

class LibroForm(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=100)
    autor = forms.CharField(label="Autor", max_length=100)
    editorial = forms.CharField(label="Editorial", max_length=100)
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_de_publicacion = forms.DateField(label="fecha_de_publicacion", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1940'}))
    isbn = forms.IntegerField(label="ISBN")

class EditorialForm(forms.Form):
    nombre_editorial = forms.CharField(label="nombre_editorial", max_length=100)
    pais_editorial = forms.CharField(label="pais_editorial", max_length=100)
    email = forms.EmailField(label="Email")

class BuscarAutoresForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")
