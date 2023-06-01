from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import EditProjectForm, RegisterProjectForm
from .models import Project_SC


# Create your views here.
class RegisterProjectView(LoginRequiredMixin, FormView):
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


class EditProjectView(LoginRequiredMixin, View):
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


class DeleteProjectView(LoginRequiredMixin, View):
    # success_url = reverse_lazy("biblioteca:register-project-edit")
    model = Project_SC
    success_url = "biblioteca:delete-project"
    template_name = "delete_project.biblioteca_sc.html"

    def get(self, request, *args, **kwargs):
        form = EditProjectForm(request=request)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = EditProjectForm(request.POST, request=request)
        if form.is_valid():
            data = form.cleaned_data

            # return redirect(self.success_url, id=data["projects"].id)
            self.model.objects.get(id=data["projects"].id).delete()
            print("➡ Se elimino correctamente")
            # Save the form and redirect

        return redirect(self.success_url)
