from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import EditProjectForm, RegisterProjectForm
from .models import Project_SC, Tutores


# Create your views here.
class RegisterProjectView(LoginRequiredMixin, FormView):
    form_class = RegisterProjectForm
    model = Project_SC
    template_name = "register_project.biblioteca_sc.html"
    success_url = reverse_lazy("biblioteca:register-project")

    def get(self, request, *args, **kwargs):

        if kwargs.get("id"):
            project = Project_SC.objects.get(id=kwargs.get("id"))
            form = self.form_class(data=project.__dict__,request=request)

        else:
            form = self.form_class(request=request)


        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = self.get_form()


        if form.is_valid():
            if kwargs.get("id"):
                return self.update_element(request, form, kwargs.get("id"))
            else:
                return self.form_valid(request, form)

        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, request, form):
        project = self.model(**form.cleaned_data)
        project.coordinador = self.request.user
        project.area = self.request.user.area
        project.save()
        messages.success(request, "Proyecto cargado correctamente.")
        return redirect(self.success_url)

    def update_element(self, request, form, id):
        data = form.cleaned_data
        model = self.model.objects.get(id=id)

        # area = usuario.tutor

        model.titulo = data["titulo"]
        model.autor = data["autor"]
        model.tutor = data["tutor"]
        model.periodo = data["periodo"]
        model.resumen = data["resumen"]
        model.ubicacion_servicio = data["ubicacion_servicio"]

        if data["file"]:
            model.file = data["file"]
        else:
            data.pop("file")

        model.save(update_fields=list(data.keys()))
        messages.success(request, "Proyecto actualizado correctamente.")

        return redirect("biblioteca:register-project-edit", id=id)


class EditProjectView(LoginRequiredMixin, View):
    success_url = "biblioteca:register-project-edit"
    template_name = "edit_project.biblioteca_sc.html"

    def get(self, request, *args, **kwargs):
        form = EditProjectForm(request=request)
        messages.info(request, "Seleccione un proyecto para proceder a editar.")
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = EditProjectForm(request.POST, request=request)
        if form.is_valid():
            data = form.cleaned_data
            return redirect(self.success_url, id=data["projects"].id)

        return render(request, self.template_name, {"form": form})


class DeleteProjectView(LoginRequiredMixin, View):
    model = Project_SC
    success_url = "biblioteca:delete-project"
    template_name = "delete_project.biblioteca_sc.html"

    def get(self, request, *args, **kwargs):
        form = EditProjectForm(request=request)
        messages.info(request, "Seleccione un proyecto para proceder a eliminar.")
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = EditProjectForm(request.POST, request=request)
        if form.is_valid():
            data = form.cleaned_data
            self.model.objects.get(id=data["projects"].id).delete()
            messages.success(request, "Proyecto eliminado correctamente.")

        return redirect(self.success_url)
