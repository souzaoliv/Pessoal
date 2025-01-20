from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import Blacklist
from .forms import BlacklistForm



# Create your views here.
class IndexView(TemplateView):
    template_name = 'blacklist/index.html'



class PlataformaView(LoginRequiredMixin, TemplateView):
    template_name = 'blacklist/plataforma.html'
    login_url = 'blacklist:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlacklistForm()
        context['blacklist'] = Blacklist.objects.filter(user=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        form = BlacklistForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data['ip_address']
            Blacklist.objects.create(user=request.user, ip_address=ip_address)
        return redirect('blacklist:plataforma')
    

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'blacklist/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blacklist:plataforma')
        return render(request, 'blacklist/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'blacklist/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blacklist:plataforma')
        return render(request, 'blacklist/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('blacklist:index')

def remove_ip(request, ip_id):
    ip = get_object_or_404(Blacklist, id=ip_id, user=request.user)
    if request.method == 'POST':
        ip.delete()
    return redirect('blacklist:plataforma')