from django.forms import ModelForm
from .models import Project_SC


class RegisterProjectForm(ModelForm):
    class Meta:
        model = Project_SC
        fields = ["titulo", "autor", "tematica", "tutor", "periodo", "area", "file"]
