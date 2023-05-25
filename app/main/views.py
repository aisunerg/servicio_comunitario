from django.shortcuts import render
from django.views import View

from biblioteca_SC.models import Project_SC


# Create your views here.
class IndexView(View):
    template_name = "index.main.html"
    model = Project_SC

    def get(self, request, *args, **kwargs):
        proyectos = self.model.objects.all()

        print("➡ proyectos :", proyectos)

        context = {"proyectos": proyectos}
        return render(request, self.template_name, context=context)

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
