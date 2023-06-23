import django.forms as forms
from .models import Project_SC, Tutores


class RegisterProjectForm(forms.ModelForm):
    class Meta:
        model = Project_SC
        fields = ["titulo", "autor", "tutor", "periodo", "file", "resumen", "ubicacion_servicio"]
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(RegisterProjectForm, self).__init__(*args, **kwargs)
        if self.request:
            self.fields["tutor"].queryset = Tutores.objects.filter(area=self.request.user.area)

    tutor = forms.ModelChoiceField(queryset=Tutores.objects.none())  

class EditProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(EditProjectForm, self).__init__(*args, **kwargs)
        if self.request:
            self.fields["projects"].queryset = Project_SC.objects.filter(coordinador=self.request.user)

    projects = forms.ModelChoiceField(queryset=Project_SC.objects.none())
