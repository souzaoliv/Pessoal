from django.urls import path
from .views import IndexView, PlataformaView, testar_senhas
app_name = 'bruteforce'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('plataforma/', PlataformaView.as_view(), name='plataforma'),
    path('testar_senhas/', testar_senhas, name='testar_senhas'),

]