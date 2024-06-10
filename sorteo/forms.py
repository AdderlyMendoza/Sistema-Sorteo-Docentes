from django import forms
from .models import Asignacion, Docentes, Area

class AsignarDocenteForm(forms.Form):
    codigo_docente = forms.IntegerField(label="Código del Docente")
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label="Área")

    def clean_codigo_docente(self):
        codigo = self.cleaned_data['codigo_docente']
        try:
            self.cleaned_data['docente'] = Docentes.objects.get(codigo=codigo)
        except Docentes.DoesNotExist:
            raise forms.ValidationError("Docente con este código no existe.")
        return codigo

    def clean(self):
        cleaned_data = super().clean()
        area = cleaned_data.get("area")
        docente = cleaned_data.get("docente")

        if area and area.asignaciones.count() >= area.cantidad:
            raise forms.ValidationError(f"La capacidad máxima para el área {area.area} ha sido alcanzada.")
        if docente and Asignacion.objects.filter(docente=docente).exists():
            raise forms.ValidationError("Este docente ya ha sido asignado a un área.")
        return cleaned_data