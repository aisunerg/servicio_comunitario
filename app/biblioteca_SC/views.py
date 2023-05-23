from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView


from .forms import RegisterProjectForm
from .models import Project_SC


# Create your views here.
class RegisterProjectView(FormView):
    form_class = RegisterProjectForm
    model = Project_SC
    template_name = "register_project.biblioteca_sc.html"
    success_url = reverse_lazy("biblioteca:register-project")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST, request.FILES)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
            # return self.render_to_response(self.get_context_data(form=form))

        else:
            print("➡ form :", form)
            return self.render_to_response(self.get_context_data(form=form))
            # return self.form_invalid(form)

    def form_valid(self, form):
        print(self.request.user)

        project = self.model(**form.cleaned_data)
        project.coordinador = self.request.user
        print("➡ project :", project)
        project.save()
        return redirect(self.success_url)


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
