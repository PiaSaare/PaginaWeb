from django.shortcuts import render
from .models import Alumno,Genero
# Create your views here.



def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos": alumnos}
    return render(request, 'alumnos/index.html', context)

def libretas(request):
    alumnos= Alumno.objects.all()
    context={"libretas": alumnos}
    return render(request, 'alumnos/libretas.html', context)

def about(request):
    alumnos= Alumno.objects.all()
    context={"about": alumnos}
    return render(request, 'alumnos/about.html', context)

def agendas(request):
    alumnos= Alumno.objects.all()
    context={"agendas": alumnos}
    return render(request, 'alumnos/agendas.html', context)

def carrito(request):
    alumnos= Alumno.objects.all()
    context={"carrito": alumnos}
    return render(request, 'alumnos/carrito.html', context)

def cuadernos(request):
    alumnos= Alumno.objects.all()
    context={"cuadernos": alumnos}
    return render(request, 'alumnos/cuadernos.html', context)

def libretasPerso(request):
    alumnos= Alumno.objects.all()
    context={"libretasPersonalizadas": alumnos}
    return render(request, 'alumnos/libretasPersonalizadas.html', context)

def registro(request):
    alumnos= Alumno.objects.all()
    context={"registro": alumnos}
    return render(request, 'alumnos/registro.html', context)

def stylesheet(request):
    alumnos= Alumno.objects.all()
    context={"stylesheet": alumnos}
    return render(request, 'alumnos/CSS/styles.css', context)

def logo(request):
    alumnos= Alumno.objects.all()
    context={"logo": alumnos}
    return render(request, 'alumnos/Images/Logo.png', context)















def crud(request):
    alumnos= Alumno.objects.all()
    context={"alumnos": alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="6"

        objGenero=Genero.objects.get(id_genero=genero)
        obj=Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo="6"
        )
        obj.save() 
        context={'mensaje':"Ok, datos grabados..."}
    return render(request, 'alumnos/alumnos_add.html', context)

