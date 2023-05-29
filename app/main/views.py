from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator

from biblioteca_SC.models import Project_SC
from authentication.forms import LoginForm



# Create your views here.
class IndexView(View):
    form_login = LoginForm
    form_filter1 = None
    form_filter2 = None  

    row_for_page = 2

    template_name = "index.main.html"
    model = Project_SC

    def get(self, request, *args, **kwargs):
        form_login = self.form_login()


        proyectos_list = self.model.objects.all()
        paginator = Paginator(proyectos_list, self.row_for_page)

        pagina = request.GET.get('pagina')
        proyectos = paginator.get_page(pagina)

        context={'proyectos': proyectos, "form_login": form_login}
        return render(request, self.template_name, context=context)
    
    def post(self, request, *args, **kwargs):
        form_login = self.form_login(request.POST)

        proyectos_list = self.model.objects.all()
        paginator = Paginator(proyectos_list, self.row_for_page)

        pagina = request.GET.get('pagina')
        proyectos = paginator.get_page(pagina)



        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(email=data['email'], password=data['password'])
            if user:
                login(request,user)
                return redirect("main:home")
            
            context={'proyectos': proyectos, "form_login": form_login}
            return render(request, self.template_name, context=context)
            
        return redirect("main:home")

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
