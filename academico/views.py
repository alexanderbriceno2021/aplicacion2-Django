from django.shortcuts import render

# Create your views here.
from .models import Curso


def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListados})
