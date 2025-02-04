from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

# Create your views here.

class IndexView(TemplateView):
    template_name = 'authenticate/index.html'

class PlataformaView(LoginRequiredMixin, TemplateView):
    template_name = 'authenticate/plataforma.html'
    login_url = 'authenticate:login'

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'authenticate/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)

            # Redirecionamento padrão caso não haja "next"
            return redirect('authenticate:plataforma')
        return render(request, 'authenticate/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'authenticate/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)

            # Redirecionamento padrão caso não haja "next"
            return redirect('authenticate:plataforma')
        return render(request, 'authenticate/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('app:index')
