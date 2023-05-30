import django.forms as forms
from .models import Project_SC


class RegisterProjectForm(forms.ModelForm):
    class Meta:
        model = Project_SC
        fields = ["titulo", "autor", "tematica", "tutor", "periodo", "file", "resumen", "ubicacion_servicio"]
        # fields = ["titulo", "autor", "tematica", "tutor", "periodo", "area", "tipo_proyecto", "file", "resumen", "ubicacion_servicio"]


class EditProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(EditProjectForm, self).__init__(*args, **kwargs)
        if self.request:
            self.fields["projects"].queryset = Project_SC.objects.filter(coordinador=self.request.user)

    projects = forms.ModelChoiceField(queryset=Project_SC.objects.none())

    # class Meta:
    #     model = Project_SC
    #     fields = ["titulo", "autor", "tematica", "tutor", "periodo", "file", "resumen", "ubicacion_servicio"]
    # fields = ["titulo", "autor", "tematica", "tutor", "periodo", "area", "tipo_proyecto", "file", "resumen", "ubicacion_servicio"]
