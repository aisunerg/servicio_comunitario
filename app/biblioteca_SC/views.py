from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView


from .forms import EditProjectForm, RegisterProjectForm
from .models import Project_SC


# Create your views here.
class RegisterProjectView(FormView):
    form_class = RegisterProjectForm
    model = Project_SC
    template_name = "register_project.biblioteca_sc.html"
    success_url = reverse_lazy("biblioteca:register-project")

    def get(self, request, *args, **kwargs):
        if kwargs.get("id"):
            project = Project_SC.objects.get(id=kwargs.get("id"))
            form = self.form_class(data=project.__dict__)

        else:
            form = self.form_class()

        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            if kwargs.get("id"):
                return self.update_element(form, kwargs.get("id"))
            else:
                return self.form_valid(form)

            # return self.render_to_response(self.get_context_data(form=form))

        else:
            print("➡ form :", form)
            return self.render_to_response(self.get_context_data(form=form))
            # return self.form_invalid(form)

    def form_valid(self, form):
        project = self.model(**form.cleaned_data)
        project.coordinador = self.request.user
        project.area = self.request.user.area
        project.save()
        return redirect(self.success_url)

    def update_element(self, form, id):
        data = form.cleaned_data
        model = self.model.objects.get(id=id)
        print("➡ data :", data)

        print(model.id)

        print("➡ self.request.user.area :", self.request.user.area)

        model.titulo = data["titulo"]
        model.autor = data["autor"]
        model.tematica = data["tematica"]
        model.tutor = data["tutor"]
        model.periodo = data["periodo"]
        model.resumen = data["resumen"]
        model.ubicacion_servicio = data["ubicacion_servicio"]

        if data["file"]:
            model.file = data["file"]
        else:
            data.pop("file")

        model.save(update_fields=list(data.keys()))
        # self.model.objects.filter(id=id).update(**data)

        return redirect("biblioteca:register-project-edit", id=id)


class EditProjectView(View):
    # success_url = reverse_lazy("biblioteca:register-project-edit")
    success_url = "biblioteca:register-project-edit"
    template_name = "edit_project.biblioteca_sc.html"

    def get(self, request, *args, **kwargs):
        form = EditProjectForm(request=request)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = EditProjectForm(request.POST, request=request)
        if form.is_valid():
            data = form.cleaned_data

            return redirect(self.success_url, id=data["projects"].id)
            print("➡ form :", form.cleaned_data)
            # Save the form and redirect

        #     return redirect('success_url')
        return render(request, self.template_name, {"form": form})


class IndexView(View):
    template_name = "index.biblioteca_sc.html"
    model = Project_SC

    def get(self, request, *args, **kwargs):
        projectos = self.model.objects.all()

        print("➡ projectos :", projectos[0].file.name)
        print("➡ projectos :", projectos[0].file.url)

        return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
