from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# MVC La Vista es la parte que se le muestra al usuario, en MVT es el Template
#     El Controlador recibe todas las peticiones del usuario, en MVT es la Vista
# MVC = Modelo [Vista   ] [Controlador => Acciones  (metodos)]
# MVT = Modelo [Template] [Vista => Acciones  (metodos)]


def index(request):
    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return render(request, "index.html")


def hola_mundo(request):
    html = """
        <h1>Hola mundo con Django!!!</h1>
        <h2>Soy Víctor Robles WEB</h2>
        <hr />
    """
    return render(request, "hola-mundo.html")


#def pagina(request, redirigir=0):
def pagina(request, redirigir=0):
    
    """
        if redirigir == 1:
            return redirect("contacto", "Pedro")
    
    """

    if redirigir == 1:
        return render(request, "contacto.html")
    else:        
        return render(request, "pagina.html")


def contacto(request, nombre="Juan", apellido="Bimba"):
    return render(request, "contacto.html")
