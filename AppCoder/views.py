from django.shortcuts import render ,redirect , get_object_or_404
from AppCoder.models import Curso,Alumno
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
# Create your views here.


def inicio(request):
    return render(request,"padre.html")


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos }
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def curso_formulario(request):
    if request.method =="POST":

        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            curso = Curso(nombre=datos["nombre"].capitalize() , camada = datos["camada"])
            curso.save()
            return render(request,"formulario.html")
            

    return render(request, "formulario.html")


def buscar_curso(request):
    return render(request,"buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
        query = request.GET.get('nombre')
        cursos = Curso.objects.filter(nombre__icontains=query)
        return render(request,"resultado_busqueda.html",{"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

def elimina_curso(request, id):
    
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso= Curso.objects.all()

    return render(request, "cursos.html", {"cursos" : curso})


def editar(request,id):
    
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre= datos["nombre"]
            curso.camada= datos["camada"]
            curso.save()

            curso=Curso.objects.all()

            return render(request, "cursos.html", {"cursos":curso})



    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})

    return render(request, "editar_curso.html", {"mi_formulario":mi_formulario , "curso":curso})



def alta_alumno(request):
    cursos = Curso.objects.all()
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'formulario_alumno.html', {'form': form, 'cursos': cursos})



def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos }
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def buscar_alumno(request):
    return render(request,"buscar_alumno.html")

def busqueda(request):
    if request.GET["dni"]:
        query = request.GET.get('dni')
        alumnos = Alumno.objects.filter(dni__icontains=query)
        return render(request,"resultado_busqueda_alumno.html",{"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el DNI del alumno.")


def eliminar_alumno(request,id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno= Alumno.objects.all()

    return render(request, "alumnos.html", {"alumnos" : alumno})

def editar_alumno(request,id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        
        form = AlumnoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            alumno.nombre= datos["nombre"]
            alumno.apellido= datos["apellido"]
            alumno.correo= datos["correo"]
            alumno.dni= datos["dni"]
            alumno.curso= datos["curso"]
            alumno.save()

            alumno=Alumno.objects.all()

            return render(request, "alumnos.html", {"alumnos":alumno})

    else:
        form = AlumnoForm(initial={"nombre":alumno.nombre, "apellido":alumno.apellido, "correo":alumno.correo, "dni":alumno.dni, "curso":alumno.curso})
        return render(request, "editar_alumno.html", {"form":form , "alumno":alumno})


def alumnos_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    alumnos = Alumno.objects.filter(curso=curso)
    return render(request, 'alumnos_curso.html', {'curso': curso, 'alumnos': alumnos})



def ver_profes(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores }
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alta_profe(request):
    cursos = Curso.objects.all()
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = ProfesorForm()
    return render(request, 'formulario_profesores.html', {'form': form, 'cursos': cursos})


def editar_profe(request,id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        
        form = ProfesorForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            profesor.nombre= datos["nombre"]
            profesor.apellido= datos["apellido"]
            profesor.correo= datos["correo"]
            profesor.dni= datos["dni"]
            profesor.curso= datos["curso"]
            profesor.save()

            profesor=Profesor.objects.all()

            return render(request, "profesores.html", {"profesores":profesor})

    else:
        form = ProfesorForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "correo":profesor.correo, "dni":profesor.dni, "curso":profesor.curso})
        return render(request, "editar_profe.html", {"form":form , "profesor":profesor})



def eliminar_profe(request,id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor= Profesor.objects.all()

    return render(request, "profesores.html", {"profesores" : profesor})


def buscar_profe(request):
    return render(request,"buscar_profe.html")


def resultado_busqueda_p(request):

    if request.GET["dni"]:
        query = request.GET.get('dni')
        profesores = Profesor.objects.filter(dni__icontains=query)
        return render(request,"resultado_busqueda_p.html",{"profesores":profesores})
    else:
        return HttpResponse("Ingrese el DNI del profesor.")
    

def profesores_curso(request,curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    profesores = Profesor.objects.filter(curso=curso)
    return render(request, 'profesores_curso.html', {'curso': curso, 'profesores': profesores})
