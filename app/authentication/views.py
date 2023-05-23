from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import LoginForm
from django.views.generic.edit import FormView
# Create your views here.
User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    template_name = "authentication_signin.html"
    # success_url = reverse_lazy('biblioteca:register-project')
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.cleaned_data
            print("➡ data :", data)
            user = authenticate(email=data['email'], password=data['password'])
            print("➡ user :", user)
            if user:
                login(request,user)
                # return redirect('authentication:colo')
                return self.render_to_response(self.get_context_data(form=form))
        
        return self.render_to_response(self.get_context_data(form=form, error="Username or password is incorrect"))
               
        
class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('authentication:login')

