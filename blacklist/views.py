from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
class IndexView(TemplateView):
    template_name = 'blacklist/index.html'

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'blacklist/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blacklist:index')
        return render(request, 'blacklist/register.html', {'form': form})
