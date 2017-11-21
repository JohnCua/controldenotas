from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from .forms import GradoForm
from control.models import Grado, Pensum


def grado_nuevo(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for materia_id in request.POST.getlist('materias'):
                pensum = Pensum(materia_id=materia_id, grado_id = grado.id)
                pensum.save()
            messages.add_message(request, messages.SUCCESS, 'Grado registrado')
    else:
        formulario = GradoForm()
    return render(request, 'control/pensum_edit.html', {'formulario': formulario})
