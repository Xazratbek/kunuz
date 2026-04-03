from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as DjangoLoginView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class LoginView(DjangoLoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def logout_view(request):
    logout(request)
    return redirect('login')
