from project.settings.base import *




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',          # Para quando o app estiver rodando localmente
    'https://lucasgso.com.br',        # Para o domínio principal com HTTPS
    'https://www.lucasgso.com.br'     # Para o subdomínio com HTTPS
]

ALLOWED_HOSTS = ['*']