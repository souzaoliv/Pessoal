from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class IndexView(TemplateView):
    template_name = 'bruteforce/index.html'


class PlataformaView(LoginRequiredMixin, TemplateView):
    template_name = 'bruteforce/plataforma.html'
    login_url = 'authenticate:login'
    
    
    
