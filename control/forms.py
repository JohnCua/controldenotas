from django import forms
from .models import Pensum, Materia ,Grado

class MateriaForm(forms.ModelForm):
        class Meta:
            model = Materia
            fields = ('nombre',)


class GradoForm(forms.ModelForm):

    class Meta:
        model = Grado
        fields = ('nombre', 'seccion', 'materias')


    def __init__ (self, *args, **kwargs):
            super(GradoForm, self).__init__(*args, **kwargs)
            self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["materias"].help_text = "Ingrese materias"
            self.fields["materias"].queryset = Materia.objects.all()
