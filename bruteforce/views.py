from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'bruteforce/index.html'


class PlataformaView(LoginRequiredMixin, TemplateView):
    template_name = 'bruteforce/plataforma.html'
    login_url = 'authenticate:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UploadFileForm()  # Passando o formulário para o template
        context['uploaded_file'] = UploadedFile.objects.last()  # Pega o último arquivo enviado (se houver)
        return context
    
    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)  # Captura os arquivos enviados
        
        if form.is_valid():
            # Salva o arquivo no banco de dados
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user  # Relacionando o arquivo ao usuário logado
            uploaded_file.save()

            messages.success(request, 'Arquivo enviado com sucesso!')

            return redirect('bruteforce:plataforma')  # Redireciona para a página da plataforma após o upload
        else:
            return render(request, 'bruteforce/plataforma.html', {'form': form})


def testar_senhas(request):
    """
    Função para testar senhas do arquivo enviado e exibir o resultado no template.
    """
    uploaded_file = UploadedFile.objects.last()  # Pega o último arquivo enviado

    if not uploaded_file:
        messages.error(request, "Nenhum arquivo foi encontrado.")
        return redirect('bruteforce:plataforma')

    senhas_encontradas = []

    try:
        with uploaded_file.file.open("r") as f:
            senhas = f.read().splitlines()

        # Testa cada senha para cada usuário
        for user in User.objects.all():
            for senha in senhas:
                user_test = authenticate(username=user.username, password=senha)
                if user_test is not None:
                    senhas_encontradas.append({"usuario": user.username, "senha": senha})
                    break  # Se encontrou a senha correta para esse usuário, pula para o próximo

        return render(request, 'bruteforce/resultados.html', {'senhas_encontradas': senhas_encontradas})

    except Exception as e:
        messages.error(request, f"Ocorreu um erro: {str(e)}")
        return redirect('bruteforce:plataforma')

