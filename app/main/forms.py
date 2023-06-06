import django.forms as forms
from authentication.models import Area
from biblioteca_SC.models import Project_SC

class FilterForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request", None)
    #     super(FilterForm, self).__init__(*args, **kwargs)
    #     if self.request:
    #         # proyectos = Project_SC.objects.all()
    #         # list_periodo = []
    #         # for proyecto in proyectos:
    #         #     list_periodo.append(proyecto.periodo) 
    #         self.fields["areas"].queryset = Area.objects.all()
    #         # self.fields["tematicas"].queryset = Area.objects.all()
    #         # self.fields["periodos"].queryset = Area.objects.all()

    areas = forms.ModelMultipleChoiceField(
        queryset = Area.objects.all(), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
    )
    #tematica = forms.ModelChoiceField(queryset=Area.objects.none())
    # periodo = forms.ModelChoiceField(queryset=Area.objects.none())    