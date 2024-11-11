from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreatingForm
from .models import CustomUser


# Create your views here.

def index(request):
     return render(
         request,
         'index.html'
     )

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта.')
    return redirect('login')

class Registration(generic.CreateView):
    template_name = 'main/register.html'
    form_class = CustomUserCreatingForm
    success_url = reverse_lazy('login')

def profile_view(request):
    return render(request, 'main/profile.html')
