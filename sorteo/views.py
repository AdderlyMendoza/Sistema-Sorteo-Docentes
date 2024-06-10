from django.shortcuts import render, redirect
from .forms import AsignarDocenteForm
from .models import Asignacion

def asignar_docente(request):
    if request.method == 'POST':
        form = AsignarDocenteForm(request.POST)
        if form.is_valid():
            docente = form.cleaned_data['docente']
            area = form.cleaned_data['area']
            Asignacion.objects.create(docente=docente, area=area)
            return redirect('sorteo:lista_asignaciones')
    else:
        form = AsignarDocenteForm()
    return render(request, 'asignar_docente.html', {'form': form})

def lista_asignaciones(request):
    asignaciones = Asignacion.objects.select_related('docente', 'area').all()
    return render(request, 'lista_asignaciones.html', {'asignaciones': asignaciones})