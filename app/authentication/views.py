from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import LoginForm
from django.views.generic.edit import FormView
# Create your views here.
User = get_user_model()

               
        
class LogoutView(FormView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main:home')

