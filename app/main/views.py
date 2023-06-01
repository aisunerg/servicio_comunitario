from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

from biblioteca_SC.models import Project_SC
from biblioteca_SC.utils.driver_connection import get_id_from_url
from authentication.forms import LoginForm


# Create your views here.
class IndexView(View):
    form_login = LoginForm
    form_filter1 = None
    form_filter2 = None
    row_for_page = 10

    template_name = "index.main.html"
    model = Project_SC

    def get_projects(self, request):
        proyectos_list = self.model.objects.get_queryset().order_by("periodo")
        paginator = Paginator(proyectos_list, self.row_for_page)
        pagina = request.GET.get("pagina")
        return paginator.get_page(pagina)

    def get(self, request, *args, **kwargs):
        context = {}
        if request.GET.get("next"):
            context["showFormLogin"] = "show"

        form_login = self.form_login()
        proyectos = self.get_projects(request)

        context["form_login"] = form_login
        context["proyectos"] = proyectos

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form_login = self.form_login(request.POST)
        proyectos = self.get_projects(request)

        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(email=data["email"], password=data["password"])
            if user:
                login(request, user)
                return redirect("main:home")

            context = {"proyectos": proyectos, "form_login": form_login}
            return render(request, self.template_name, context=context)

        return redirect("main:home")

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')


class DocumentDetailView(View):
    form_login = LoginForm
    model = Project_SC
    template_name = "document-details.main.html"

    def get(self, request, *args, **kwargs):
        print("➡ kwargs :", kwargs)
        form_login = self.form_login()

        proyecto = self.model.objects.get(id=kwargs["id"])
        try:
            id_file = get_id_from_url(proyecto.file.url)
            file_url = f"https://drive.google.com/file/d/{id_file}/preview"
        except:
            file_url = None

        context = {"form_login": form_login, "proyecto": proyecto, "file_url": file_url}
        return render(request, self.template_name, context=context)
